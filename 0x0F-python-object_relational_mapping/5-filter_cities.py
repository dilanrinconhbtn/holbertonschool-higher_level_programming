#!/usr/bin/python3
import MySQLdb
import sys


def selection(a, b, c, d):
    """selection from table states order by id states and just letter N"""
    db = MySQLdb.connect(user=a, passwd=b, db=c, port=3306)
    cur = db.cursor()
    cur.execute("""SELECT cities.name
    FROM cities
    JOIN states ON states.id = cities.state_id
    WHERE states.name = %(d)s
    ORDER BY cities.id""", {'d': d})

    show = cur.fetchall()
    i = 0
    for x in show:
        if i is not 0:
            print(", ", end='')
        print(x[0], end='')
        i += 1
    print()
    """close connection"""
    cur.close()
    db.close()

if __name__ == '__main__':
    selection(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
