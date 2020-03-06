import os
import urllib.parse as up
import psycopg2
import urlparse3
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer
from base import Base

database_url = "postgres://qouisghc:AW7QV02qj3HK6ayULidW044XexiNrklW@balarama.db.elephantsql.com:5432/qouisghc"

engine = create_engine(database_url)
Session = sessionmaker(bind=engine)

base = declarative_base()
engine.connect()


class word(Base):
    __tablename__ = 'words'

    id = Column(Integer, primary_key=True)
    word = Column(String)
    defination = Column(String)
    koen = Column(String)
    boejninger = Column(String)

    def __init__(self, word, defination, koen, boejninger):




Base.metadata.create_all(engine)
session = Session()
abe = word("abe", "substantiv", "intetkøn", "-en")
session.add(abe)
session.commit()
session.close()
# up.uses_netloc.append("postgres")
# url = urlparse3.parse_url(os.environ[database_url])
# conn = psycopg2.connect(database=url.path[1:],
#                       user=url.username,
#                      password=url.password,
#                     host=url.hostname,
#                    port=url.port)
# conn = psycopg2.connect("dbname='words' user='qouisghc' host='balarama.db.elephantsql.com:5432' password='ZIP_8LxWXvWoqs-tClZ4tLgY2w3Rr6E9'")
