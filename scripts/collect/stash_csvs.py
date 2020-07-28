#!/usr/bin/env python

"""
split_csvs.py - takes the raw CSVs and splits them into year-by-year files,
    if the raw CSV is bigger than 25MB

Requires one argument, expects it to be a directory:

    ./collect/split_csvs.py data/collected/unpacked.csvs/2020-07-27

"""

from sys import path as syspath; syspath.append('./scripts')
from myutils import mylog, myinfo, mywarn, existed_size


import csv
from sys import argv
from pathlib import Path
import re

DATA_DIR = Path('data', 'collected', 'osha', 'snapshots')
DEST_DIR = Path('data', 'collected', 'osha', 'stash')

DEFAULT_ROW_COUNT = 100000


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

    master_header = None

    for c_i, cname in enumerate(cnames):
        mylog(cname.name, label="Reading")
        with open(cname) as cfile:
            cdata = csv.DictReader(cfile)
            if c_i > 0:
                if master_header != cdata.fieldnames:
                    raise ValueError(f"Fieldnames {cdata.fieldnames} did not match master header: {master_header}")
            else:
                master_header = cdata.fieldnames

            for row in cdata:
                yield row


def stash_glom(glom, glom_name, destdir, index_field=None):
    """
    glom is an iteration of uniform dicts, e.g. from a bunch of similar CSV files

    glom_name is something like 'osha_accident_abstract'

    Files are written to:
        destdir/glom_name/glom_name-0001.csv
    """

    glomdir = destdir.joinpath(glom_name)
    glomdir.mkdir(exist_ok=True, parents=True)

    file_count = 0
    current_file = None
    current_csv = None

    for i, row in enumerate(glom):
        if i % DEFAULT_ROW_COUNT == 0:
            # time to start a new file
            if current_file:
                current_file.close()
            _destpath = glomdir.joinpath(f"{glom_name}-{str(file_count).rjust(4, '0')}.csv")
            myinfo(_destpath, label="New stash")
            file_count += 1

            current_file = open(_destpath, 'w')
            current_csv = csv.DictWriter(current_file, fieldnames=row.keys())
            current_csv.writeheader()
        current_csv.writerow(row)

    if current_file and current_file.closed != True:
        current_file.close()





def main(main_srcdir, main_destdir):
    # destdir.mkdir(exist_ok=True, parents=True)
    for srcdir in [d for d in main_srcdir.glob('*') if d.is_dir()]:
        glomname = srcdir.name
        glom = glom_csvs(srcdir.glob('*.csv'))
        stash_glom(glom, glomname, main_destdir)


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

    myinfo(DEST_DIR, label="Stash destination")

    main(srcdir, DEST_DIR)
