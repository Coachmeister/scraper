import sqlite3
from sqlite3 import Error
import cursor



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
        :return: Connection object or None
        """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    database = r"C:\Development\python\scraper\scraperdata.db"

    sql_create_word_table = """CREATE TABLE IF NOT EXIST(
    id integer PRIMARY KEY,
    word text,
    defination text,
    køn text,
    bøjning text
    );"""

    #create a db connection
    conn = create_connection(database)

    #create table
    if conn is not None:
        create_table(conn, sql_create_word_table)
