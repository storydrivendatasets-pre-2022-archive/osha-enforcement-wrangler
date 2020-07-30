#!/usr/bin/env python

"""
fetch_zips.py

Reads data/MANIFEST.yaml, and for each entry where autocollect==true, downloads from the
  corresponding `url`

"""
from sys import path as syspath; syspath.append('./scripts')
from utils.mylog import *

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



def fetch(url):
    """
    easy downloading function: provides progress bar
    https://stackoverflow.com/questions/37573483/progress-bar-while-download-file-over-http-with-requests
    """
    resp = requests.get(url, stream=True)
    content_length = int(resp.headers.get('content-length', 0))
    blocksize = 1024
    progress_bar = tqdm(total=content_length, unit='iB', unit_scale=True)

    for datablock in resp.iter_content(blocksize):
        progress_bar.update(len(datablock))
        yield datablock
    progress_bar.close()


def fetch_and_save(url, destpath):
    xb = existed_size(destpath)
    purl = Path(url)
    if xb:
        mylog(f"{destpath}", f"{xb} bytes", label="Exists")
        mylog(purl.name, purl.parent, label="Skipping")
    else:
        mylog(purl.name, purl.parent, label="Downloading")
        resp = fetch(url)
        destpath.parent.mkdir(exist_ok=True, parents=True)
        with open(destpath, 'wb') as dest:
            for data in resp:
                dest.write(data)

        mylog(destpath, f"{existed_size(destpath)} bytes", label="Saved")




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
