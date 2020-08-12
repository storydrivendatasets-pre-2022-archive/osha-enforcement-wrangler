#!/usr/bin/env python

"""
collect/unpack_zips.py

Has an optional argument for src directory; by default, it takes the latest
    directory in data/collected/snapshots

Unzips all zips into individual subdirs of data/collected/snapshots/YYYY-MM-DD/unpacked/

For unzipped filenames that have a number, e.g. 'osha_violation_event2.csv', they are
unzipped as: 'osha_violation_event_2.csv'


"""
from sys import path as syspath

syspath.append("./scripts")
from utils.myfiler import existed_size, get_latest_snapshot_dir
from utils.mylog import *

from pathlib import Path
import re
from sys import argv
from zipfile import ZipFile


def main(srcdir, destdir):
    def _dest_name(fname):
        rx = re.search(r"(.+?)(\d+)\.(\w+)$", fname)
        if rx:
            rx = rx.groups()
            # we need to rename/renumber the file for its destpath
            fname = "{}-{}.{}".format(rx[0], rx[1].rjust(3, "0"), rx[2])
        return fname

    zipnames = sorted(list(srcdir.glob("*.zip")))
    myinfo(f"Found {len(zipnames)} zipfiles")

    for zn in zipnames:
        # we actually make a subdir for each zip file
        _zsub = re.search(r"(\w+)_\d{8}", zn.stem).groups()[0]
        zdir = destdir.joinpath(_zsub)
        zdir.mkdir(exist_ok=True, parents=True)

        mylog(zn, label="Unpacking")
        zfile = ZipFile(zn)
        zlist = sorted(zfile.filelist, key=lambda x: x.filename)
        for _z in zlist:
            zname = _z.filename
            fname = _dest_name(zname) if len(zfile.filelist) > 1 else zname
            destpath = zdir.joinpath(fname)
            destpath.write_bytes(zfile.read(zname))
            mylog(
                destpath.name,
                destpath.parent,
                f"{existed_size(destpath)} bytes",
                label="Extracted",
            )


if __name__ == "__main__":
    if len(argv) < 2:
        srcdir = get_latest_snapshot_dir().joinpath("zips")
    else:
        srcdir = Path(argv[1])
        if not srcdir.is_dir():
            raise ValueError(f"Expected 1st argument to be a directory: {srcdir}")

    myinfo(srcdir, label="Source dir")

    targetdir = srcdir.parent.joinpath("unpacked")
    myinfo(targetdir, label="Unpacked destination")

    main(srcdir, targetdir)
