#!/usr/bin/python3
""" import modules"""
import sys
import MySQLdb


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    search = sys.argv[4].split(';', 1)[0]
    cur.execute("SELECT * FROM states WHERE name = {} ORDER BY states.id".format(search))
    query_rows = cur.fetchall()
    for state in query_rows:
        print(state)
    cur.close()
    conn.close()