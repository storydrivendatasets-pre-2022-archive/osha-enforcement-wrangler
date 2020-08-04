#!/usr/bin/env python3
from sys import path as syspath; syspath.append('./scripts')
from utils.mylog import *
from utils.mydb import connect_to_db, create_tables

from pathlib import Path
import re

SRC_DB_PATH = Path('data/compiled/osha_compiled.sqlite')
TARGET_DB_PATH = Path('data/wrangled/osha_wrangled.sqlite')

CREATE_DB_PATH = Path('scripts/wrangle/create_wrangled_schema.sql')
INSERTS_DIR = Path('scripts/wrangle/inserts')
INDEXES_PATH = Path('scripts/wrangle/index_wrangled.sql')

def index_table(connection):
    mylog(INDEXES_PATH, label="Indexing tables")
    stmt = INDEXES_PATH.read_text()
    connection.cursor().execute()



def inserts(connection):
    cursor = connection.cursor()
    cursor.execute(f"ATTACH DATABASE '{SRC_DB_PATH}' AS src_db;")
    cursor.execute(f"ATTACH DATABASE '{TARGET_DB_PATH}' AS target_db;")

    for insertpath in sorted(INSERTS_DIR.glob('*.sql')):
        mylog(insertpath, label="Running insert")
        stmt = insertpath.read_text()
        cursor.execute(stmt)

def main():
    TARGET_DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    mylog(TARGET_DB_PATH, label="Connecting to")
    conn = connect_to_db(TARGET_DB_PATH)

    mylog("Creating tables")
    create_tables(conn, schema_path=CREATE_DB_PATH)
    inserts(conn)

    conn.close()

if __name__ == '__main__':
    main()
