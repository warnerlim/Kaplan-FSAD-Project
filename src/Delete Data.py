import sqlite3

def deleteMultipleRecords(idList):
    try:
        sqliteConnection = sqlite3.connect('students.db3')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sqlite_update_query = """DELETE from Math where StudentUUID = ?"""

        cursor.executemany(sqlite_update_query, idList)
        sqliteConnection.commit()
        print("Total", cursor.rowcount, "Records deleted successfully")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to delete multiple records from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")

idsToDelete = [("S00017",), ("S000018",)]
deleteMultipleRecords(idsToDelete)