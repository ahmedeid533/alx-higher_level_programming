#!/usr/bin/python3
""" import modules"""
import sys
import MySQLdb


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM \
                cities INNER JOIN states ON states.id=cities.state_id")
    query_rows = cur.fetchall()
    tmp_rows = list(row1[0] for row1 in query_rows)
    print(*tmp_rows, sep=", ")
    cur.close()
    conn.close()
