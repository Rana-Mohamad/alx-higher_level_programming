#!/usr/bin/python3
'''
takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
is safe from MySQL injections
'''
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    rows_num = cur.execute("SELECT * FROM states WHERE name=%s\
                            ORDER BY states.id", (argv[4], ))
    for x in range(rows_num):
        print(cur.fetchone())