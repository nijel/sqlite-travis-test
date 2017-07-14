import sqlite3

with open('test.sql', 'r') as handle:
    test = handle.read()
with sqlite3.connect(':memory:') as sql:
#    sql.executescript(test)
    sql.isolation_level = None
    sql.execute('PRAGMA temp_store=MEMORY;')
    sql.execute('PRAGMA page_size=1024;')
    sql.execute('BEGIN;')
    sql.execute('CREATE TABLE t1(x INTEGER PRIMARY KEY, y TEXT);')
    for x in range(250):
        sql.execute("INSERT INTO t1(x,y) VALUES ({0}*10, printf('%04d%.800c',{0},'*'))".format(x))
    sql.execute('SAVEPOINT one;')
    sql.execute('SELECT count(*) FROM t1;')
    for x in range(250):
        sql.execute("INSERT INTO t1(x,y) VALUES ({0}*10 + 1, printf('%04d%.800c',{0},'*'))".format(x))
    sql.execute('ROLLBACK TO one;')
    sql.execute('SELECT count(*) FROM t1;')
    sql.execute('SAVEPOINT twoB;')
    for x in range(10):
        sql.execute("INSERT INTO t1(x,y) VALUES ({0}*10+2, printf('%04d%.800c',{0},'*'))".format(x))
    sql.execute('ROLLBACK TO twoB;')
    sql.execute('COMMIT;')
