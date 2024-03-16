import sqlite3
import random as rd
def insertMultipleRecords(recordList):
    try:
        sqliteConnection = sqlite3.connect('students.db3')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_insert_query = """INSERT INTO Science
                          (StudentUUID, ScienceCA1, ScienceSA1, ScienceCA2, ScienceSA2) 
                          VALUES (?, ?, ?, ?, ?);"""

        cursor.executemany(sqlite_insert_query, recordList)
        sqliteConnection.commit()
        print("Total", cursor.rowcount, "Records inserted successfully into SqliteDb_developers table")
        sqliteConnection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert multiple records into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

Marks = ("S000001", rd.randint(50,100),rd.randint(50,100),rd.randint(50,100),rd.randint(50,100))


recordsToInsert = [(Marks)]

insertMultipleRecords(recordsToInsert)