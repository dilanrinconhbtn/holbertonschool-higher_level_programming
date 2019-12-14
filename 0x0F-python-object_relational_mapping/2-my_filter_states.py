#!/usr/bin/python3
import MySQLdb
import sys


def selection(a, b, c, d):
    """selection from table states order by id states and just letter N"""
    db = MySQLdb.connect(user=a, passwd=b, db=c, port=3306)
    cur = db.cursor()
    cur.execute("""SELECT * FROM states
    WHERE name = '{}'
    ORDER BY states.id ASC""".format(d))
    show = cur.fetchall()
    for x in show:
        print(x)
    """close connection"""
    cur.close()
    db.close()

if __name__ == '__main__':
    selection(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
