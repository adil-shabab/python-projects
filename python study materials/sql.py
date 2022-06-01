from sqlite3 import Cursor
import mysql.connector as ms


mydb = ms.connect(
    host = 'localhost',
    user = 'root',
    password = 'HACKER@3197',
    database = 'irfan'
)


# create a cursor object 
Cursor = mydb.cursor()


# sql queries 
Cursor.execute(
    """
    create table class5(
        roll int,
        name varchar(20),
        mark int
    )
    """
)