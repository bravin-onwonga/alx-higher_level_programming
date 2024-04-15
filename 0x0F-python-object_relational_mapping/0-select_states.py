#!/usr/bin/python3
"""
Module to list state.name ordered by id
"""

import sys
import MySQLdb


if __name__ == "__main__":
    username, password, dbName = sys.argv[1:]
    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=dbName, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
