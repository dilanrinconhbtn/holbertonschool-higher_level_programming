#!/usr/bin/python3
import MySQLdb
import sys


def selection(a, b, c):
    """selection from table states order by id states"""
    db = MySQLdb.connect(user=a, passwd=b, db=c, port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    show = cur.fetchall()
    for x in show:
        print(x)
    """close connection"""
    cur.close()
    db.close()

if __name__ == '__main__':
    selection(sys.argv[1], sys.argv[2], sys.argv[3])
