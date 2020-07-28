#!/usr/bin/env python

"""
split_csvs.py - takes the raw CSVs and splits them into year-by-year files,
    if the raw CSV is bigger than 25MB

Requires one argument, expects it to be a directory:

    ./collect/split_csvs.py data/collected/unpacked.csvs/2020-07-27

"""

from sys import path as syspath; syspath.append('./scripts')
import csv
from sys import argv

DATA_DIR = Path('data', 'collected', 'osha',)

def main(srcdir, destdir):
    mylog('FUn!')
    # DEST_DIR.mkdir(exist_ok=True, parents=True)
    # catalog_urls = fetch_catalog_urls()
    # myinfo(f"Fetched {len(catalog_urls)} catalog urls")

    # for url in catalog_urls:
    #     fetch_and_save(url, destpath(url))



if __name__ == '__main__':
    if len(argv) < 2:
        # assume data/collected/2020-07-27 (i.e. latest dir) is the working
        # directory
        datadirs = [p for p in DATA_DIR.glob('*/unpacked/') if p.is_dir() and re.search(r'\d{4}-\d{2}-\d{2}', str(p))]
        if not datadirs:
            raise ValueError(f"Could not find any valid collected unpacked directories in {DATA_DIR}")
        else:
            srcdir = sorted(datadirs)[-1]
    else:
        srcdir = Path(argv[1])
        if not srcdir.is_dir():
            raise ValueError(f"Expected 1st argument to be a directory: {srcdir}")
    myinfo(srcdir, label="Source dir")

    datedir = srcdir.parent.name # srcdir is expected to be dest/to/foo/2020-07-20/zips
    destdir = DATA_DIR.joinpath(datedir, 'unpacked')
    myinfo(destdir, label="Unpacked destination")

    main(srcdir, destdir)
