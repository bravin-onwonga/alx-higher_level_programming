#!/usr/bin/python3
"""
Module to list row based on arg passed
"""

import sys
import MySQLdb


if __name__ == "__main__":
    username, password, dbName = sys.argv[1:]
    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=dbName, charset="utf8")
    cur = conn.cursor()
    query = "SELECT * FROM cities JOIN states ON \
        cities.state_id = states.id ORDER BY cities.id ASC"
    cur.execute(query)
    query_rows = cur.fetchall()
    for row in query_rows:
        print("({}, '{}', '{}')".format(row[0], row[2], row[4]))
    cur.close()
    conn.close()
