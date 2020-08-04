#!/usr/bin/env python3
# DATA_DIR='data/compiled/osha/raw'
from sys import path as syspath; syspath.append('./scripts')
from utils.mylog import *
from utils.mydb import connect_to_db, create_tables, import_table_from_csv

from pathlib import Path
import re

SRC_DIR = Path('data/compiled/osha/raw')
TARGET_DB_PATH = Path('data/compiled/osha_compiled.sqlite')

CREATE_PATH = Path('scripts/compile/create_compiled_schema.sql')
INDEXES_PATH = Path('scripts/compile/index_compiled.sql')

SKIPPED_FILES = ('data_dictionary', 'metadata',)




def get_data_paths():
    paths = sorted(p for p in SRC_DIR.glob('*.csv')
                    if all(_sk not in p.name
                    for _sk in SKIPPED_FILES))
#   return [p for p in paths if 'osha_vio' in  p.name]
    return paths


def index_table(connection):
    mylog(INDEXES_PATH, label="Indexing tables")
    stmt = INDEXES_PATH.read_text()
    connection.cursor().execute(stmt)



def main():
    mylog(TARGET_DB_PATH, label="Connecting to")
    conn = connect_to_db(TARGET_DB_PATH)

    mylog("Creating tables")
    create_tables(conn, schema_path=CREATE_PATH)

    srcpaths = get_data_paths()
    for srcpath in srcpaths:
        import_table_from_csv(conn, srcpath)

    index_table(conn)
    conn.close()

if __name__ == '__main__':
    main()
