# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# ##Test out UGRID-0.9 compliant unstructured grid model datasets with PYUGRID

# <codecell>

import matplotlib.tri as tri
import datetime as dt

# <codecell>

import cartopy.crs as ccrs
import iris
iris.FUTURE.netcdf_promote = True
import pyugrid

# <codecell>

from thredds_crawler.crawl import Crawl

# <codecell>

catalog='http://comt.sura.org/thredds/comt_2_current.xml'
catalog='http://comt.sura.org/thredds/comt_1_archive_summary.xml'
#c = Crawl(catalog, select=[".*-Agg"])
c = Crawl(catalog)

print c.datasets

# <codecell>

dap_urls = [s.get("url") for d in c.datasets for s in d.services if s.get("service").lower() == "opendap"]

# <codecell>

ugrid=[]
cf=[]
not_cf=[]
for url in dap_urls:
    print url
    try:
        ug = pyugrid.UGrid.from_ncfile(url)
        ugrid.append(url)
    except:
        print 'not a ugrid'

    try:
        cube = iris.load_cube(url,'sea_surface_height_above_geoid')
        cf.append(url)
    except:
        not_cf.append(url)

# <codecell>

len(ugrid)

# <codecell>

len(cf)

# <codecell>

len(not_cf)

# <codecell>


