#!/usr/bin/env python3
"""
build-map-data.py — regenerates MAP_GEO, the baked geometry of the Headwaters Ledger home map.

THIS IS NOT PART OF THE PAGE. index.html never loads it and never will; the tool remains a single
file that runs from a double-click with no build step. This script exists because MAP_GEO is
machine output — 45 KB of SVG path data rounded to a tenth of a viewBox unit — and data nobody can
hand-edit needs a way to be made again.

  python3 -m pip install rasterio fiona shapely matplotlib numpy pillow
  python3 tools/build-map-data.py > mapdata.json

Then paste the result into index.html as the argument to JSON.parse in the MAP_GEO block.

SOURCES, all fetched over plain HTTPS, all public domain or equivalent:
  boundaries  Natural Earth 1:50m admin-1 (states + provinces), via the nvkelso/natural-earth-vector
              mirror on GitHub. The only reachable source found that carries Canadian provinces —
              Natural Earth's 1:110m admin-1 file is United States only.
  divides     USGS Watershed Boundary Dataset, HUC2 regions, read by byte-range out of the zipped
              GeoPackages staged on prd-tnm.s3.amazonaws.com. Range-reading them takes about five
              minutes and no disk; downloading the same ten regions is 2.5 GB.
  terrain     Copernicus GLO-90 DEM, 1-degree COG tiles on AWS Open Data.

THE ONE THING TO KNOW BEFORE CHANGING ANYTHING: the Albers parameters below are duplicated in
index.html (MAP_ALBERS), because the page projects the headwaters pins at runtime from the lon/lat
already in its data block rather than storing a second copy of them in viewBox units. Change a
parameter here and you must change it there, or the pins will land somewhere plausible and wrong.
"""
import json, math, os, pickle, sys, time
import numpy as np
from concurrent.futures import ThreadPoolExecutor

os.environ.update({
    'GDAL_DISABLE_READDIR_ON_OPEN': 'EMPTY_DIR',
    # .zip and .gpkg are load-bearing: the WBD divides are range-read out of zipped
    # GeoPackages, and with only .tif allowed GDAL refuses to open them.
    'CPL_VSIL_CURL_ALLOWED_EXTENSIONS': '.tif,.zip,.gpkg',
    'VSI_CACHE': 'TRUE',
})
import rasterio, fiona, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from shapely.geometry import shape, box, LineString, Polygon
from shapely.ops import unary_union, linemerge

def log(*a): print(*a, file=sys.stderr)

# ---------------------------------------------------------------- projection
# Albers equal-area conic. EQUAL AREA is the point, not a preference: the tiled-block map this
# replaced drew British Columbia at roughly Montana's size, and BC is 944,000 km2 to Montana's
# 381,000. Equalising them is the same flattening the per-region pies make and that the continental
# card exists to correct, so the map that opens the tool should not be repeating it.
LAT1, LAT2, LAT0, LON0 = 43.0, 55.0, 45.0, -119.0
_R = math.radians
_n = (math.sin(_R(LAT1)) + math.sin(_R(LAT2))) / 2.0
_C = math.cos(_R(LAT1))**2 + 2*_n*math.sin(_R(LAT1))
def _rho(lat): return math.sqrt(max(0.0, _C - 2*_n*math.sin(_R(lat)))) / _n
_rho0 = _rho(LAT0)
def albers(lon, lat):
    th = _n * _R(lon - LON0); r = _rho(lat)
    return (r*math.sin(th), _rho0 - r*math.cos(th))

VB   = 900.0
SIX  = ['British Columbia','Alberta','Montana','Idaho','Wyoming','Colorado']
KEY  = {'British Columbia':'bc','Alberta':'ab','Montana':'mt',
        'Idaho':'id','Wyoming':'wy','Colorado':'co'}
NE   = ('https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/'
        'ADMIN1.geojson')
NE50 = NE.replace('ADMIN1', 'ne_50m_admin_1_states_provinces')
WBD  = 'https://prd-tnm.s3.amazonaws.com/StagedProducts/Hydrography/WBD/HU2/GPKG/'
COP  = 'https://copernicus-dem-90m.s3.amazonaws.com/'

# ---------------------------------------------------------------- boundaries
def load_admin1(path='ne50_admin1.geojson'):
    if not os.path.exists(path):
        import urllib.request
        log('fetching Natural Earth 50m admin-1 ...')
        urllib.request.urlretrieve(NE50, path)
    d = json.load(open(path))
    return {f['properties']['name']: shape(f['geometry']) for f in d['features']
            if f['properties'].get('admin') in ('Canada', 'United States of America')}

# ---------------------------------------------------------------- the divides
# Which side of the Continental Divide each HUC2 region falls on. The Colorado (14, 15) drains to
# the Gulf of California and the Great Basin (16) drains nowhere at all, but both sit WEST of the
# Divide — the Divide is about which way water runs off the ridge, not where it finally ends up.
PACIFIC  = ['14','15','16','17','18']
ATLANTIC = ['09','10','11','12','13']

def huc2(hu):
    """Read one HUC2 boundary by byte-range out of its zipped GeoPackage on S3."""
    p = '/vsizip//vsicurl/%sWBD_%s_HU2_GPKG.zip/WBD_%s_HU2_GPKG.gpkg' % (WBD, hu, hu)
    with fiona.open(p, layer='WBDHU2') as src:
        return shape(next(iter(src))['geometry'])

def shared_boundary(g1, g2, tol=0.01):
    """The line two basin groups have in common — i.e. the divide between them.

    An exact boundary intersection SHATTERS wherever the two polygons' vertices do not coincide.
    Through Montana that turned one 6-degree divide into eleven sub-half-degree crumbs, which the
    length filter then discarded, leaving a divide with a hole in it that still looked plausible.
    Asking "which of g1's boundary lies within tol of g2" is the robust question."""
    keep = g1.boundary.intersection(g2.buffer(tol))
    parts = [g for g in getattr(keep, 'geoms', [keep]) if g.geom_type == 'LineString']
    m = unary_union(parts)
    m = linemerge(m) if m.geom_type != 'LineString' else m
    return sorted(getattr(m, 'geoms', [m]), key=lambda l: -l.length)

def continental_divide(prov):
    log('reading 10 HUC2 regions by range-read (about 5 minutes) ...')
    with ThreadPoolExecutor(max_workers=10) as ex:
        hu = dict(zip(PACIFIC + ATLANTIC, ex.map(huc2, PACIFIC + ATLANTIC)))
    P = unary_union([hu[k].buffer(0) for k in PACIFIC])
    A = unary_union([hu[k].buffer(0) for k in ATLANTIC])
    lines = [l for l in shared_boundary(P, A) if l.length > 1.0]
    log('  US divide: %d segment(s), longest %.1f deg' % (len(lines), lines[0].length))

    # The Canadian stretch. The BC/Alberta boundary IS the Continental Divide from the 49th
    # parallel to about 54N — and from there north it is the 120th meridian, a survey line and not
    # a watershed. Drawing the whole boundary as "the Divide" would be a 6-degree lie, so the
    # meridian stretch is cut where it begins.
    keep = prov['Alberta'].boundary.intersection(prov['British Columbia'].buffer(0.03))
    segs = [g for g in getattr(keep, 'geoms', [keep]) if g.geom_type == 'LineString']
    m = unary_union(segs)
    m = linemerge(m) if m.geom_type != 'LineString' else m
    ab = sorted(getattr(m, 'geoms', [m]), key=lambda l: -l.length)[0]
    cs = list(ab.coords)
    cut = next((i for i, (lo, la) in enumerate(cs) if lo <= -119.999 and la >= 53.9), len(cs))
    log('  BC/AB divide-following stretch: %.1fN to %.1fN' % (cs[0][1], cs[cut-1][1]))
    return lines + [LineString(cs[:cut])]

# NOT BUILT, ON PURPOSE: the Northern (Hudson Bay) Divide. WBD is a US dataset, so the only part
# available is the Souris-Red stretch out in the Dakotas — the half that matters here, running west
# from Triple Divide Peak, is in Canada, where no comparable data is reachable. Half a divide drawn
# as though it were whole is the kind of quiet lie the project's data rules exist to stop.

# ---------------------------------------------------------------- terrain
DEM_BOX  = (-141, -100, 35, 62)     # lon0, lon1, lat0, lat1
DEM_STEP = 0.04                      # degrees; ~4 km, and about 3x finer than the map can show
LEVELS   = [1000, 2000, 3000]        # metres

def dem_grid():
    lon0, lon1, lat0, lat1 = DEM_BOX
    W = int((lon1-lon0)/DEM_STEP); H = int((lat1-lat0)/DEM_STEP); ppt = int(1/DEM_STEP)
    grid = np.full((H, W), np.nan, np.float32)
    def url(lat, lon):
        ew = ('W%03d' % -lon) if lon < 0 else ('E%03d' % lon)
        n = 'Copernicus_DSM_COG_30_N%02d_00_%s_00_DEM' % (lat, ew)
        return '/vsicurl/%s%s/%s.tif' % (COP, n, n)
    def grab(a):
        lat, lon = a
        try:
            with rasterio.open(url(lat, lon)) as ds:
                x = ds.read(1, out_shape=(ppt, ppt)).astype(np.float32)
                if ds.nodata is not None: x[x == ds.nodata] = np.nan
                return lat, lon, x
        except Exception:
            return lat, lon, None       # ocean tiles simply do not exist in the bucket
    jobs = [(la, lo) for la in range(lat0, lat1) for lo in range(lon0, lon1)]
    t0 = time.time(); ok = 0
    with ThreadPoolExecutor(max_workers=32) as ex:
        for lat, lon, x in ex.map(grab, jobs):
            if x is None: continue
            ok += 1
            grid[(lat1-1-lat)*ppt:(lat1-lat)*ppt, (lon-lon0)*ppt:(lon-lon0+1)*ppt] = x
    log('  %d/%d DEM tiles in %.0fs' % (ok, len(jobs), time.time()-t0))
    grid[np.isnan(grid)] = 0
    # a light box blur, so the contours come out as terrain rather than as lace
    k = 3; pad = np.pad(grid, k, mode='edge'); sm = np.zeros_like(grid)
    for dy in range(-k, k+1):
        for dx in range(-k, k+1):
            sm += pad[k+dy:k+dy+H, k+dx:k+dx+W]
    return sm / (2*k+1)**2

# ---------------------------------------------------------------- assembly
def main():
    prov = load_admin1()
    # Frame: the six regions' own vertices in projected space, plus a 5% margin.
    xs, ys = [], []
    for n in SIX:
        g = prov[n]
        for p in (g.geoms if g.geom_type == 'MultiPolygon' else [g]):
            for lo, la in p.exterior.coords:
                x, y = albers(lo, la); xs.append(x); ys.append(y)
    X0, X1, Y0, Y1 = min(xs), max(xs), min(ys), max(ys)
    mx, my = (X1-X0)*0.10, (Y1-Y0)*0.10
    X0 -= mx; X1 += mx; Y0 -= my; Y1 += my
    FRAME = box(0, 0, VB, VB)

    def P(lon, lat):
        x, y = albers(lon, lat)
        # y flips: Albers y counts north, SVG y counts down.
        return ((x-X0)/(X1-X0)*VB, (Y1-y)/(Y1-Y0)*VB)

    def path_of(coords, close):
        d = []; prev = None
        for i, (a, b) in enumerate(coords):
            xy = (round(a, 1), round(b, 1))
            if prev == xy: continue
            d.append(('M' if prev is None else 'L') + ('%g,%g' % xy)); prev = xy
        return ''.join(d) + ('Z' if close else '')

    def emit(g, tol, close=True, projected=False):
        """Project, clip to the frame, simplify IN SCREEN UNITS so the tolerance means the same
           thing everywhere on the map, and write SVG path data."""
        out = []
        for p in (g.geoms if hasattr(g, 'geoms') else [g]):
            rings = [p.exterior] + list(p.interiors) if p.geom_type == 'Polygon' else [p]
            for r in rings:
                xy = list(r.coords) if projected else [P(a, b) for a, b in r.coords]
                q = Polygon(xy) if close else LineString(xy)
                if close and not q.is_valid: q = q.buffer(0)
                q = q.intersection(FRAME)
                if q.is_empty: continue
                for s in (q.geoms if hasattr(q, 'geoms') else [q]):
                    if s.is_empty or s.geom_type not in ('Polygon', 'LineString'): continue
                    s = s.simplify(tol, preserve_topology=False)
                    cs = list(s.exterior.coords) if s.geom_type == 'Polygon' else list(s.coords)
                    if len(cs) < (4 if close else 2): continue
                    if close and s.area < 6: continue      # drop specks under a few pixels
                    out.append(path_of(cs, close))
        return ''.join(out)

    data = {'vb': VB, 'frame': [round(v, 7) for v in (X0, X1, Y0, Y1)]}

    log('terrain ...')
    dem = dem_grid()
    fig, ax = plt.subplots()
    cs = ax.contourf(dem, levels=LEVELS + [1e9])
    bands = []
    for coll in cs.get_paths():
        segs = []
        for poly in coll.to_polygons(closed_only=True):
            if len(poly) < 4: continue
            xy = [P(DEM_BOX[0] + a*DEM_STEP, DEM_BOX[3] - b*DEM_STEP) for a, b in poly]
            q = Polygon(xy)
            if not q.is_valid: q = q.buffer(0)
            segs.append(emit(q, 0.9, projected=True))
        bands.append(''.join(segs))
    data['bands'] = bands

    log('boundaries ...')
    data['regions'] = {KEY[n]: emit(prov[n], 0.25) for n in SIX}
    near = [n for n, g in prov.items() if n not in SIX and g.intersects(box(-142, 33, -98, 62))]
    data['near'] = ''.join(emit(prov[n], 0.9) for n in near)
    # The union of every admin-1 polygon in frame doubles as the coastline — which is why there is
    # no second, coarser coast outline on this map to disagree with the boundaries drawn over it.
    data['land'] = emit(unary_union([prov[n].buffer(0) for n in prov]), 0.6)

    log('rivers and lakes ...')
    import urllib.request
    for nm, url in (('rivers','ne_50m_rivers_lake_centerlines'), ('lakes','ne_50m_lakes')):
        f = url + '.geojson'
        if not os.path.exists(f):
            urllib.request.urlretrieve(NE.replace('ADMIN1', url), f)
        gj = json.load(open(f))
        close = (nm == 'lakes')
        data[nm] = ''.join(emit(shape(x['geometry']), 0.35, close=close) for x in gj['features']
                           if not shape(x['geometry']).is_empty)

    log('divides ...')
    data['divide'] = ''.join(emit(l, 0.3, close=False) for l in continental_divide(prov))

    lab = {}
    for n in SIX:
        g = prov[n]
        big = max((g.geoms if g.geom_type == 'MultiPolygon' else [g]), key=lambda p: p.area)
        pt = big.centroid
        if not big.contains(pt): pt = big.representative_point()
        x, y = P(pt.x, pt.y); lab[KEY[n]] = [round(x, 1), round(y, 1)]
    data['lab'] = lab

    out = json.dumps(data, separators=(',', ':'))
    for k in ('bands', 'land', 'regions', 'near', 'rivers', 'lakes', 'divide'):
        log('  %-9s %7d bytes' % (k, len(json.dumps(data[k], separators=(',', ':')))))
    log('TOTAL %d bytes' % len(out))
    # NO trailing newline. This gets pasted between the single quotes of a JSON.parse() call
    # in index.html, and a raw newline inside a JS string literal is a syntax error that
    # takes the whole page down. sys.stdout.write, not print.
    sys.stdout.write(out)

if __name__ == '__main__':
    main()
