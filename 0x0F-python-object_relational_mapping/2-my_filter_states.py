#!/usr/bin/python3
"""
Lists all states with a name starting with 'N'
from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <name_starts_with>"
              .format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    name_starts_with = sys.argv[4] + '%'

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    new_cursor = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
    new_cursor.execute(query, (name_starts_with,))
    rows = new_cursor.fetchall()
    for row in rows:
        print(row)
    new_cursor.close()
    db.close()
