from pathlib import Path
import re

SNAPSHOTS_DATA_DIR = Path('data', 'collected', 'snapshots')


def existed_size(path):
    e = Path(path)
    if e.is_file():
        return e.stat().st_size
    else:
        return False


def get_latest_snapshot_dir():
    # assume data/collected/2020-07-27 (i.e. latest dir) is the working
    # directory
    datadirs = [p for p in SNAPSHOTS_DATA_DIR.glob('*/') if p.is_dir() and re.search(r'\d{4}-\d{2}-\d{2}', str(p))]
    if not datadirs:
        raise ValueError(f"Could not find any valid collected zip directories in {SNAPSHOTS_DATA_DIR}")
    else:
        srcdir = sorted(datadirs)[-1]
        return srcdir
