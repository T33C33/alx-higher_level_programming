#!/usr/bin/python3
"""lists all states with a name starting with N (upper N)
"""


if __name__ == "__main__":
    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database)

    cursor = db.cursor()
    string = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    cursor.execute(string)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
