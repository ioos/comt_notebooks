# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# COMT Standards Compliance Test

# <markdowncell>

# Crawl a THREDDS catalog, and try loading all OPeNDAP urls with pyugrid and Iris

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

# <codecell>

name_list=['water_surface_height_above_reference_datum',
    'sea_surface_height_above_geoid','sea_surface_elevation',
    'sea_surface_height_above_reference_ellipsoid','sea_surface_height_above_sea_level',
    'sea_surface_height','water level']

# <codecell>

def name_in_list(cube):
    return cube.standard_name in name_list

# <codecell>

name_constraint = iris.Constraint(cube_func=name_in_list)

# <codecell>

def my_test(cube):
    return cube.standard_name in name_list & cube.cell_methods[0].method=='point'

# <codecell>

def my_func(cube):
    b = False
    if cube.standard_name in name_list:
        if hasattr(cube,'cell_methods'):
            b = not any(m.method == 'maximum' for m in cube.cell_methods)
        else:
            b = True
    return b

# <codecell>

my_constraint = iris.Constraint(cube_func=my_func)

# <codecell>

dap_urls = [s.get("url") for d in c.datasets for s in d.services if s.get("service").lower() == "opendap"]

# <codecell>

ugrid=[]
not_ugrid=[]
cf=[]
not_cf=[]
for url in dap_urls:
    try:
        ug = pyugrid.UGrid.from_ncfile(url)
        ugrid.append(url)
    except:
        not_ugrid.append(url)

    try:
        cube = iris.load_cube(url,my_constraint)
        cf.append(url)
    except:
        not_cf.append(url)

# <codecell>

len(ugrid)

# <codecell>

len(not_ugrid)

# <codecell>

len(cf)

# <codecell>

len(not_cf)

