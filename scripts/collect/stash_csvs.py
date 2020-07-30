#!/usr/bin/env python

"""
stash_csvs.py - for each subdirectory (i.e. series) of data in:
     data/collected/osha/snapshots/YYYY-MM-DD/unpacked

Creates re-sliced copies in: data/collected/osha/stash

The unpacked data is re-sliced (into files of DEFAULT_SLICE_COUNT rows each), if:
    - There's more than one file in the series
    - Or, if there's one file and it's bigger than SINGLE_FILE_SIZE_THRESHOLD

Has an optional argument, if you want to specify a specific snapshot of unpacked data

    ./collect/stash_csvs.py data/collected/osha/snapshots/2020-07-27/unpacked

"""

from sys import path as syspath; syspath.append('./scripts')
from utils.mylog import *

import csv
from sys import argv
from pathlib import Path
import re

DATA_DIR = Path('data', 'collected', 'osha', 'snapshots')
TARGET_DIR = Path('data', 'collected', 'osha', 'stash')

# Number of rows to arbitrarily split a file by
DEFAULT_SLICE_COUNT = 100000

# for data that is a single file, this is max bytes we allow that single file to be
# before splitting it up
SINGLE_FILE_SIZE_THRESHOLD = 15000000

def glom_csvs(csvnames):
    """
    csvnames is a list of Path objects, assumed to belong to
        all the same types of data, e.g.
            osha_violation0.csv
            osha_violation1.csv
            osha_violation2.csv
            osha_violation3.csv

    glom_csvs processes each separate CSV file in order, making sure the headers are uniform,
        and yields each row as a dict
    """


    cnames = sorted(csvnames)
    mylog(f'{len(cnames)} files; first is {cnames[0].name}', label="Glomming")

    FIRST_HEADER = None

    def verify_header_integrity(header, idx):
        """
        When opening a new CSV in a series, we check the header against
        the "FIRST_HEADER", e.g. the header for the first CSV file in the series
        """
        nonlocal FIRST_HEADER
        if idx == 0:
            # first file in a series sets the FIRST_HEADER
            FIRST_HEADER = header
        else:
            if FIRST_HEADER != header:
                raise ValueError(f"Fieldnames {header} did not match first header in series: {FIRST_HEADER}")


    for series_idx, cname in enumerate(cnames):
        mylog(f"{series_idx}. {cname.name}", f"{existed_size(cname)} bytes", label="Reading")
        with open(cname) as cfile:
            cdata = csv.DictReader(cfile)
            verify_header_integrity(cdata.fieldnames, series_idx)
            for row in cdata:
                yield row


def stash_glom(glom, glom_name, targetdir, index_field=None):
    """
    glom is an iteration of uniform dicts, e.g. from a bunch of similar CSV files

    glom_name is something like 'osha_accident_abstract'

    Files are written to:
        targetdir/glom_name/glom_name-0001.csv
    """
    file_count = 0
    file_handler = None
    current_csv = None

    def make_destpath():
        nonlocal glomdir, glom_name, file_count
        return glomdir.joinpath(f"{glom_name}-{str(file_count).rjust(4, '0')}.csv")


    def init_csv():
        """
        closes cfile if closable, returns a CSV.DictReader
        """
        nonlocal file_count, file_handler
        if file_handler:
            file_handler.close()
        destpath = make_destpath()
        myinfo(destpath, label="New stash")
        file_count += 1

        file_handler = open(destpath, 'w')
        newcsv = csv.DictWriter(file_handler, fieldnames=row.keys())
        newcsv.writeheader()
        return newcsv


    glomdir = targetdir.joinpath(glom_name)
    glomdir.mkdir(exist_ok=True, parents=True)

    for i, row in enumerate(glom):
        if i % DEFAULT_SLICE_COUNT == 0:
            current_csv = init_csv()

        current_csv.writerow(row)

    # at the end, close the open file
    if file_handler and file_handler.closed != True:
        file_handler.close()





def main(main_srcdir, main_targetdir):
    # targetdir.mkdir(exist_ok=True, parents=True)
    for datadir in [d for d in main_srcdir.iterdir() if d.is_dir()]:
        glomname = datadir.name # e.g. "osha_accident" from collected/osha/snapshots/YYYY-MM-DD/unpacked/osha_accident
        cnames = list(datadir.glob('*.csv'))

        if len(cnames) == 1 and existed_size(cnames[0]) < SINGLE_FILE_SIZE_THRESHOLD:
            # special case in which there's only one file, and it's small
            # e.g. unpacked/osha_accident_lookup2/osha_accident_lookup2.csv
            cn = cnames[0]
            myinfo(f"{cn}", f"only 1 file of {existed_size(cn)} bytes", label="Skipping glom")
            cn_destpath = main_targetdir.joinpath(glomname, cn.name)
            cn_destpath.parent.mkdir(exist_ok=True, parents=True)
            cn_destpath.write_bytes(cn.read_bytes())
            mylog(cn_destpath, label="Wrote")

        else:
            glom = glom_csvs(cnames)
            stash_glom(glom, glomname, main_targetdir)


def get_latest_snapshot_dir():
    # assume data/collected/2020-07-27 (i.e. latest dir) is the working
    # directory
    datadirs = [p for p in DATA_DIR.glob('*/unpacked/') if p.is_dir() and re.search(r'\d{4}-\d{2}-\d{2}', str(p))]
    if not datadirs:
        raise ValueError(f"Could not find any valid collected unpacked directories in {DATA_DIR}")
    else:
        srcdir = sorted(datadirs)[-1]
        return srcdir

if __name__ == '__main__':
    if len(argv) < 2:
        srcdir = get_latest_snapshot_dir()
    else:
        srcdir = Path(argv[1])
        if not srcdir.is_dir():
            raise ValueError(f"Expected 1st argument to be a directory: {srcdir}")

    myinfo(srcdir, label="Source dir")
    myinfo(TARGET_DIR, label="Stash destination")

    main(srcdir, TARGET_DIR)
