#!/usr/bin/python3
"""
Module to list row based on arg passed
"""

import sys
import MySQLdb


if __name__ == "__main__":
    username, password, dbName, state_name = sys.argv[1:]
    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=dbName, charset="utf8")
    cur = conn.cursor()
    query = "SELECT * FROM states WHERE name = '{}' \
        ORDER BY id ASC".format(state_name)
    cur.execute(query)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
