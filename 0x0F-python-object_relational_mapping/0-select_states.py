#!/usr/bin/python3
import sys
import MySQLdb


if __name__ == "__main__":
	conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
	cur = conn.cursor()
	cur.execute("SELECT * FROM states") # HERE I have to know SQL to grab all states in my database
	query_rows = cur.fetchall()
	for state in query_rows: # HERE: no SQL query, only objects!
		print(state)
	cur.close()
	conn.close()
