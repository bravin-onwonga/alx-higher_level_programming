#!/usr/bin/python3
"""
Module to list row based on arg passed
"""

import sys
import MySQLdb


if __name__ == "__main__":
    if (len(sys.argv) == 5):
        username, password, dbName, state_name = sys.argv[1:]
        conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                               passwd=password, db=dbName, charset="utf8")
        cur = conn.cursor()
        query = "SELECT name FROM cities WHERE cities.state_id = \
            (SELECT id FROM states WHERE states.name = %s) \
                ORDER BY cities.id ASC"
        cur.execute(query, (state_name,))
        query_rows = cur.fetchall()
        for i in range(len(query_rows) - 1):
            print("{}".format(query_rows[i][0]), end=", ")
        if (len(query_rows) > 0):
            print("{}".format(query_rows[len(query_rows) - 1][0]))
        else:
            print()
        cur.close()
        conn.close()
