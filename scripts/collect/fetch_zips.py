#!/usr/bin/env python

"""
fetch_zips.py

Reads data/MANIFEST.yaml, and for each entry where autocollect==true, downloads from the
  corresponding `url`

"""
from sys import path as syspath; syspath.append('./scripts')

from myutils import mylog, myinfo, mywarn, fetch_and_save

from pathlib import Path
import requests
import re
from lxml.html import fromstring as lxsoup
from urllib.parse import urlparse

CATALOG_URL = 'https://enforcedata.dol.gov/views/data_summary.php'
TARGET_DIR = Path('data', 'collected', 'osha', 'snapshots')


def targetpath(url):
    """
    Given a URL like:
    https://enfxfr.dol.gov/../data_catalog/OSHA/osha_accident_injury_20200727.csv.zip

    Create a subdir and path:
    "TARGET_DIR/2020-07-27/osha_accident_injury_20200727.csv.zip"
    """
    upath = Path(urlparse(url).path)
    bname = upath.name
    yr, mth, day = re.search(r'(\d{4})(\d{2})(\d{2})', bname).groups()
    return TARGET_DIR.joinpath(f"{yr}-{mth}-{day}", 'zips',  bname)


def fetch_catalog_urls():
    mylog(CATALOG_URL, label="Fetching catalog")
    resp = requests.post(CATALOG_URL, data={'agency': 'osha'})
    soup = lxsoup(resp.text)
    urls = soup.xpath('//a[contains(@href, "csv.zip")]/@href')
    """
    each url will look like this:
        https://enfxfr.dol.gov/../data_catalog/OSHA/osha_accident_injury_20200727.csv.zip
    so we tidy it to:
        https://enfxfr.dol.gov/data_catalog/OSHA/osha_accident_injury_20200727.csv.zip
    """
    return [u.replace('../data_catalog', 'data_catalog') for u in urls]


def main():
    TARGET_DIR.mkdir(exist_ok=True, parents=True)
    catalog_urls = fetch_catalog_urls()
    myinfo(f"Fetched {len(catalog_urls)} catalog urls")

    for url in catalog_urls:
        fetch_and_save(url, targetpath(url))

if __name__ == '__main__':
    main()
