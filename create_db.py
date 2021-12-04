import sqlite3
import os


def init_db(conn = conn):
    create_table = """
    CREATE TABLE passenger(
        id PRIMARY KEY AUTOINCREMENT,
        pclass INTEGER,
        sex VARCHAR(10),
        Age VARCHAR(30),
        SibSp INTEGER,
        Parch INTEGER,
        Embarked VARCHAR(10),
        Last_Name VARCHAR(20),
        First_Name VARCHAR(40)
    )
    """