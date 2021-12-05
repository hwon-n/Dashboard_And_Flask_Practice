import sqlite3
import os
import csv

DATABASE_NAME = 'titanic.db'
DATABASE_PATH = os.path.join(os.getcwd(), DATABASE_NAME)
CSV_FILENAME = 'titanic.csv'
CSV_FILEPATH = os.path.join(os.getcwd(), CSV_FILENAME)

conn = sqlite3.connect(DATABASE_PATH)
cur = conn.cursor()


# create table (query)

create_table = """
CREATE TABLE passenger(
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Pclass INTEGER,
    Sex VARCHAR(10),
    Age INTEGER,
    Age_Label VARCHAR(30),
    SibSp INTEGER,
    Parch INTEGER,
    Fare VARCHAR(50),
    Embarked VARCHAR(10),
    Last_Name VARCHAR(20),
    First_Name VARCHAR(40)
);
"""

drop_table = 'DROP TABLE IF EXISTS passenger;'

cur.execute(drop_table)
cur.execute(create_table)


# open csv file and insert value

insert = """
INSERT INTO passenger(Pclass, Sex, Age, Age_Label, Sibsp, Parch, Fare, Embarked, Last_Name, First_Name) 
VALUES (?, ?, ?, ? ,?, ?, ?, ?, ?, ?)
"""

with open(CSV_FILENAME) as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        if 'Pclass' in row[0]:
            pass
        else:
            values = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
            cur.execute(insert, values)

conn.commit()