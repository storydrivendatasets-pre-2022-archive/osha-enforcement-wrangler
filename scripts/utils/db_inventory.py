#!/usr/bin/env python3
from sys import path as syspath
syspath.append("./scripts")

from utils.mylog import *
from utils.mydb import connect_to_db

import apsw
import csv
from collections import defaultdict
from math import floor
from pathlib import Path
import re
from sys import argv, stdout


DEFAULT_DB_PATH = Path("data/wrangled/osha_wrangled.sqlite")

TABLE_INDEX_QUERY = """
WITH tx AS (
    SELECT
        name AS table_name
    FROM sqlite_master WHERE type='table'
    ORDER BY table_name ASC
), rx AS (
    SELECT
        tx.table_name
        , pg.name AS index_name
    FROM tx
    INNER JOIN
        PRAGMA_INDEX_LIST(tx.table_name) AS pg
), ry AS (
    SELECT rx.table_name
        , rx.index_name
        , pg.cid
        , pg.seqno
        , pg.name AS col_name
    FROM rx
    INNER JOIN
        PRAGMA_INDEX_INFO(rx.index_name) AS pg
    ORDER BY
        table_name ASC
        , cid ASC
        , seqno ASC
)
SELECT
    table_name
    , index_name
    , GROUP_CONCAT(col_name, '|') AS indexcols
FROM ry
GROUP BY
    table_name
    , index_name
;
"""



def collate_indexes(connection):
    """returns dict of lists: {tablename: [idxcol1, idxcol2, (idxcol1,idxcol2)]}"""

    def _list_indexes(connection):
        cursor = connection.cursor()
        results = cursor.execute(TABLE_INDEX_QUERY)
        headers = [h[0] for h in results.getdescription()]
        return [{h: row[i] for i, h in enumerate(headers)} for row in results]

    d = defaultdict(set)
    for row in _list_indexes(connection):
        tname = row["table_name"]
        s = d[tname]
        colstr = row["indexcols"]
        for col in colstr.split("|"):
            s.add(col)
        s.add(colstr)
    return d


def count_table_rows(connection, tablename):
    x = connection.cursor().execute(f"""SELECT COUNT(1) FROM "{tablename}";""")
    return int(x.fetchall()[0][0])


def count_colgroup_rows(connection, tablename, colgroup):
    cursor = connection.cursor()
    colq = ", ".join([f'"{c}"' for c in colgroup.split("|")])
    x = cursor.execute(
        f"""
        WITH gg AS (SELECT {colq} FROM {tablename} GROUP BY {colq})
        SELECT COUNT(1) from gg;"""
    )
    return int(x.fetchall()[0][0])


def main(dbpath):
    mylog(dbpath, label="Connecting to")
    conn = connect_to_db(dbpath)
    colindexes = collate_indexes(conn)

    outs = csv.DictWriter(
        stdout, fieldnames=("table_name", "rowcount", "colgroup", "pct_total_count")
    )
    outs.writeheader()

    for tablename, colstrings in colindexes.items():
        total_rows = count_table_rows(conn, tablename)

        outs.writerow({"table_name": tablename, "rowcount": total_rows})

        for colstr in colstrings:
            d = {"table_name": tablename, "colgroup": colstr}
            d["rowcount"] = count_colgroup_rows(conn, tablename, colstr)
            d["pct_total_count"] = floor(100.0 * d["rowcount"] / total_rows)
            outs.writerow(d)

    conn.close()


if __name__ == "__main__":
    target_db_path = argv[1] if len(argv) > 1 else None
    if target_db_path:
        main(target_db_path)
    else:
        dbpath = DEFAULT_DB_PATH
        conn = connect_to_db(dbpath)
        cursor = conn.cursor()

        main(dbpath)
        import IPython; IPython.embed()
