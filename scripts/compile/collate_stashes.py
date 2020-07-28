#!/usr/bin/env python3
"""
./compile/collate_stashes.py

Given data/collected/osha/stash/**/, reverse the file splitting
    and create single files for each data series in:
    data/compiled/raw/

How to test in bash:
    # single file
    $ diff --strip-trailing-cr data/compiled/osha/raw/osha_accident_lookup2.csv <(xsv fmt data/collected/osha/stash/osha_accident_lookup2/osha_accident_lookup2.csv)

    # big multiseries
    $ xsv cat rows data/collected/osha/stash/osha_inspection/*.csv > /tmp/xsv-cat-osha_inspection.csv
    $ diff --strip-trailing-cr data/compiled/osha/raw/osha_inspection.csv /tmp/xsv-cat-osha_inspection.csv

"""
from sys import path as syspath; syspath.append('./scripts')
from myutils import mylog, myinfo, mywarn, existed_size

import csv
from sys import argv
from pathlib import Path
import re

STASH_DIR = Path('data', 'collected', 'osha', 'stash')
DEST_DIR = Path('data', 'compiled', 'osha', 'raw')


def main():
    data_dirs = sorted(d for d in STASH_DIR.iterdir() if d.is_dir())
    myinfo(f"{STASH_DIR}", f"{len(data_dirs)} data directories", label="Main stash dir")

    DEST_DIR.mkdir(parents=True, exist_ok=True)

    # def init_csv(seriesname):
    #     """seriesname is a expected to be a string corresponding to
    #        a subdir like 'osha_violations/'
    #     """


    for datadir in data_dirs:
        src_paths = sorted(datadir.glob('*.csv'))
        myinfo(f"{datadir}", f"{len(src_paths)} files", label="Stash subdir")

        destpath = DEST_DIR.joinpath(f'{datadir.name}.csv')
        destfile = open(destpath, 'w')
        dest = csv.writer(destfile)

        _rowcount = 0
        for series_idx, srcpath in enumerate(src_paths):
            mylog(f"{series_idx}. {srcpath.name} | {existed_size(srcpath)} bytes", label="Reading")
            with open(srcpath) as srcfile:
                src = csv.reader(srcfile)
                header = next(src)
                if series_idx == 0:
                    # first file in series, include header
                    dest.writerow(header)
                for row in src:
                    dest.writerow(row)
                    _rowcount += 1
        myinfo(destpath, f"{_rowcount} rows total (+ header)", label="Wrote")
        destfile.close()

if __name__ == '__main__':
    main()
