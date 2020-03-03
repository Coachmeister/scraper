import sqlite3
from sqlite3 import Error
import cursor


def create_connection(db_file):
    """ create a database connection to the SQLite database
            specified by db_file
        :param db_file: database file
        :return: Connection object or None
        """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)

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

def create_word(conn, word):
    """create a new word
    :param conn:
    :param word
    :return: word id"""
    sql = '''INSERT INTO words(id, word, defination, koen, boejning)
             VALUES(?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, word)
    return cur.lastrowid

def main():
    database = r"C:\Development\python\scraper\scraperdata.db"

  #  sql_create_word_table = """CREATE TABLE IF NOT EXISTS words (
  #  id integer primary key,
  #  ord text,
  #  defination text,
  #  koen text,
  #  boejning text
  #  );"""

    # create a db connection
    conn = create_connection(database)
    with conn:
        word = (1, "data", "substantiv", "intetkøn", "-et, -, -ene")
    print("word added")
    #create table
#   if conn is not None:
#       create_table(conn, sql_create_word_table)
#   else:
    #   print("uhooo. no db connection")
