#!/usr/bin/env python3
from sys import path as syspath

syspath.append("./scripts")
from utils.mylog import *
from utils.mydb import connect_to_db, count_rows, create_tables

from pathlib import Path
import re

SRC_DB_PATH = Path("data/compiled/osha_compiled.sqlite")
TARGET_DB_PATH = Path("data/wrangled/osha_wrangled.sqlite")

CREATE_DB_PATH = Path("scripts/wrangle/create_wrangled_schema.sql")
INSERTS_DIR = Path("scripts/wrangle/inserts")
INDEXES_PATH = Path("scripts/wrangle/index_wrangled.sql")


def index_table(connection):
    mylog(INDEXES_PATH, label="Indexing tables")
    stmt = INDEXES_PATH.read_text()
    connection.cursor().execute()


def load_custom_functions(connection):
    def _convert_xyn_boolean(val):
        if val in ("Y", "X",):
            return True
        elif val in (None, "N",):
            return False
        else:
            raise ValueError(f"Unexpected value: `{val}`")

    def _left_zero_pad(val, num):
        if type(val) is str:
            return val.rjust(num, "0")
        else:
            return val

    def _normalize_text(val):
        """
        Expectations:
            val is a string value or None; blank strings are *not* expected
        """
        if val is None:
            return None
        elif type(val) is not str:
            raise ValueError(
                f"Got value `{val}` of type `{type(val)}`; only expecting strings"
            )
        else:
            return re.sub(" +", " ", val).strip().upper()

    connection.createscalarfunction("convert_xyn_boolean", _convert_xyn_boolean, 1)
    connection.createscalarfunction("left_zero_pad", _left_zero_pad, 2)
    connection.createscalarfunction("normalize_text", _normalize_text, 1)
    return connection


def inserts(connection):
    def _get_paths():
        return sorted(INSERTS_DIR.glob("*.sql"))

    cursor = connection.cursor()
    cursor.execute(f"ATTACH DATABASE '{SRC_DB_PATH}' AS src_db;")
    cursor.execute(f"ATTACH DATABASE '{TARGET_DB_PATH}' AS target_db;")

    srcpaths = _get_paths()
    myinfo(f"{len(srcpaths)} INSERT SQL scripts", label="File count")

    for i, insertpath in enumerate(srcpaths):
        tname = re.match(r"insert_(\w+)", insertpath.stem).groups()[0]
        targettbl = f"target_db.{tname}"
        mylog(f"#{i+1} {targettbl}", insertpath, label="Running insert")
        stmt = insertpath.read_text()
        cursor.execute(stmt)

        myinfo(f"{count_rows(cursor, targettbl)} rows in {targettbl}", label="Inserted")


def main():
    TARGET_DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    mylog(TARGET_DB_PATH, label="Connecting to")
    conn = connect_to_db(TARGET_DB_PATH)
    conn = load_custom_functions(conn)

    mylog("Creating tables")
    create_tables(conn, schema_path=CREATE_DB_PATH)
    inserts(conn)

    conn.close()


if __name__ == "__main__":
    main()
