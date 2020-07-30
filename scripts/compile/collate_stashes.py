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
from utils.mylog import *

import csv
from sys import argv
from pathlib import Path
import re

STASH_DIR = Path('data', 'collected', 'osha', 'stash')
TARGET_DIR = Path('data', 'compiled', 'osha', 'raw')


def main():

    def _fix_header(fields):
        """
        we expect every actual data table to have a "load_dt" column as its last column,
            but some tables have load_date or ld_dt
        """
        header = fields.copy()
        if fields[-1] in ('load_date', 'ld_dt',):
            header[-1] = 'load_dt'
            myinfo(f"From {fields[-1]} to {header[-1]}", label='Fixed header')
        return header

    # def init_csv(seriesname):
    #     """seriesname is a expected to be a string corresponding to
    #        a subdir like 'osha_violations/'
    #     """


    data_dirs = sorted(d for d in STASH_DIR.iterdir() if d.is_dir())
    myinfo(f"{STASH_DIR}", f"{len(data_dirs)} data directories", label="Main stash dir")

    TARGET_DIR.mkdir(parents=True, exist_ok=True)



    for datadir in data_dirs:
        src_paths = sorted(datadir.glob('*.csv'))
        myinfo(f"{datadir}", f"{len(src_paths)} files", label="Stash subdir")

        targetpath = TARGET_DIR.joinpath(f'{datadir.name}.csv')
        targetfile = open(targetpath, 'w')
        target = csv.writer(targetfile)

        _rowcount = 0
        for series_idx, srcpath in enumerate(src_paths):
            mylog(f"{series_idx}. {srcpath.name} | {existed_size(srcpath)} bytes", label="Reading")
            with open(srcpath) as srcfile:
                src = csv.reader(srcfile)
                header = next(src)

                if series_idx == 0:
                    # first file in series, write header to target
                    xheader = _fix_header(header)
                    target.writerow(xheader)
                for row in src:
                    target.writerow(row)
                    _rowcount += 1
        myinfo(targetpath, f"{_rowcount} rows total (+ header)", label="Wrote")
        targetfile.close()

if __name__ == '__main__':
    main()
