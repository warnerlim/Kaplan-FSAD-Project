import sqlite3

class Subject:
    def __init__(self,uuid,CA1,SA1,CA2,SA2):
        # Object Attributes
        self.uuid = uuid
        self.CA1 = CA1
        self.SA1 = SA1
        self.CA2 = CA2
        self.SA2 = SA2

def update_multiple_columns(StudentUUID, Subject, CA1, SA1, CA2, SA2): 
    # Function has been adapted from https://pynative.com/python-sqlite-update-table/
    # Function is used to update student's exam marks in the database
    sqliteConnection = sqlite3.connect('students.db3')
    # Connects to database ‘students.db3’ and stores it in variable sqliteConnection.
    cursor = sqliteConnection.cursor()
    # Connects to the database 'students.db3' and allows user to data manipulate anything 
    # inside the database through the temporary workstation, stores it in a variable called cursor.
    sqlite_update_query = "Update " + Subject + " set CA1 = ?, SA1 = ?, CA2 = ?, SA2 = ? where StudentUUID = ?"
    # Is a string that stores the Subject positional argument variable into the string.
    columnValues = (CA1, SA1, CA2, SA2, StudentUUID)
    # Applies the positional argument variable data inside this tuple columnValues
    cursor.execute(sqlite_update_query, columnValues)
    # The values stored in the columnValues binds it to the string sqlite_update_query. 
    # The execute is then pulling data from the database under potential subject tables 
    # such as English, Math, Chinese, Science that have the columns CA1,SA1,CA2,SA2 and StudentUUID 
    # which then promptly updates the marks of these 4 exams under the StudentUUID listed in the variable.
    sqliteConnection.commit()
    # Confirms any modifications made in the update query into the students.db3 database
    cursor.close()
    # Closes the connection to the database

def unit_test():
    update_multiple_columns("S000015", "Math", 42, 24, 98, 88)

unit_test()