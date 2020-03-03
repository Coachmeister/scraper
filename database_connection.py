import sqlite3
from sqlite3 import Error
import scrapest
import cursor

class DatabaseConnection:
    def create_connection(db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(sqlite3.version)
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()
        return conn

    def create_table(conn, create_table_sql):
        """" create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)

    def create():
        database = r"C:\Development\python\scraper\scraperdata.db"

        sql_create_word_table = """CREATE TABLE IF NOT EXIST (
        id integer PRIMARY KEY,
        word text,
        defination text,
        køn text,
        bøjning text,
        );"""
        conn = create_connection (database)

#dddddd
