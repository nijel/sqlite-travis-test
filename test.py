import sqlite3

with open('test.sql', 'r') as handle:
    test = handle.read()
with sqlite3.connect(':memory:') as sql:
    sql.executescript(test)
