import sqlite3
import os


def init_db(conn = conn):
    create_table = """
    CREATE TABLE passenger(
        id PRIMARY KEY AUTOINCREMENT,
        pclass INTEGER,
        name VARCHAR(30),
        
    )
    """