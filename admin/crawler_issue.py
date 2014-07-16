# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from thredds_crawler.crawl import Crawl

# <codecell>

catalog='http://comt.sura.org/thredds/comt_2_current.xml'
catalog='http://comt.sura.org/thredds/comt_1_archive_summary.xml'
c = Crawl(catalog)

print c.datasets

# <codecell>

dap_urls = [s.get("url") for d in c.datasets for s in d.services if s.get("service").lower() == "opendap"]

# <codecell>


