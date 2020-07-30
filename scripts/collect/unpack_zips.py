#!/usr/bin/env python

"""
collect/unpack_zips.py

Has an optional argument for src directory; by default, it takes the latest
    directory in data/collected/osha/snapshots

Unzips all zips into individual subdirs of data/collected/osha/snapshots/YYYY-MM-DD/unpacked/

For unzipped filenames that have a number, e.g. 'osha_violation_event2.csv', they are
unzipped as: 'osha_violation_event_2.csv'


"""
from sys import path as syspath; syspath.append('./scripts')
from utils.mylog import *

from pathlib import Path
import re
from sys import argv
from zipfile import ZipFile

DATA_DIR = Path('data', 'collected', 'osha', 'snapshots')


def main(srcdir, destdir):

    zipnames = list(srcdir.glob('*.zip'))
    myinfo(f"Found {len(zipnames)} zipfiles")

    def dest_filename(fname):
        rx = re.search(r'(.+?)(\d+)\.(\w+)$', fname)
        if rx:
            rx = rx.groups()
            # we need to rename/renumber the file for its destpath
            fname = '{}-{}.{}'.format(rx[0], rx[1].rjust(3, '0'), rx[2])
        return fname


    for zn in zipnames:
        # we actually make a subdir for each zip file
        _zsub = re.search(r'(\w+)_\d{8}', zn.stem).groups()[0]
        zdir = destdir.joinpath(_zsub)
        zdir.mkdir(exist_ok=True, parents=True)
        zfile = ZipFile(zn)
        for zi in zfile.filelist:
            zname = zi.filename
            fname = dest_filename(zname) if len(zfile.filelist) > 1 else zname
            destpath = zdir.joinpath(fname)
            destpath.write_bytes(zfile.read(zname))
            mylog(destpath.name, destpath.parent, f"{existed_size(destpath)} bytes", label="Extracted")



def get_latest_snapshot_dir():
    # assume data/collected/2020-07-27 (i.e. latest dir) is the working
    # directory
    datadirs = [p for p in DATA_DIR.glob('*/zips/') if p.is_dir() and re.search(r'\d{4}-\d{2}-\d{2}', str(p))]
    if not datadirs:
        raise ValueError(f"Could not find any valid collected zip directories in {DATA_DIR}")
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

    # have to derive the target dir, i.e. "unpacked subdir"
    # srcdir is expected to be something like snapshots/2020-07-01/zips
    # so corresponding destdir is snapshots/2020-07-01/unpacked
    datestr = srcdir.parent.name
    destdir = DATA_DIR.joinpath(datestr, 'unpacked')
    myinfo(destdir, label="Unpacked destination")

    main(srcdir, destdir)
