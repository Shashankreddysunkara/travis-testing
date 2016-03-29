# Simple SQL tests for playing with database setups

import unittest

try:
    import psycopg2
    DBCONN = psycopg2.connect(database='test')
except ImportError:
    import sqlite3
    DBCONN = sqlite3.connect(':memory:')


class TestSQL(unittest.TestCase):

    def setUp(self):
        cursor = DBCONN.cursor()
        try:
            cursor.execute("SELECT * FROM test;")
        except Exception:
            DBCONN.rollback()
            cursor.execute("CREATE TABLE test (id INT NOT NULL, name TEXT);")

    def test_case1(self):
        cursor = DBCONN.cursor()
        cursor.execute("INSERT INTO test (id,name) VALUES (1, 'hello');")
        self.assertEqual(cursor.rowcount, 1)

    def test_case2(self):
        cursor = DBCONN.cursor()
        cursor.execute("INSERT INTO test (id,name) VALUES (2, 'goodbye');")
        self.assertEqual(cursor.rowcount, 1)
        cursor.execute("SELECT name from test where id = 2;")
        rows = cursor.fetchall()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][0], u'goodbye')
        self.assertEqual(type(DBCONN), object)
