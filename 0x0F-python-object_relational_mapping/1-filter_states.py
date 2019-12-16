#!/usr/bin/python3
import MySQLdb
import sys


if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306)

    cur = db.cursor()
    cur.execute("""SELECT * FROM states
    WHERE name LIKE BINARY'N%'\
    ORDER BY states.id""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
