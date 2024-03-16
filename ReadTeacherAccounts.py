import sqlite3
class Teacher:
    def __init__(self,uuid,name,password):
        # Object Attributes
        self.uuid = uuid
        self.name = name
        self.password = password

def get_all_teachers_from_db(): # Function has been adapted from https://pynative.com/python-sqlite-select-from-table/
    # Function that obtain all the teacher's uuid name and password 
    # from the database students.db3 under the table TeacherAccounts
    teachers = []
    # teachers is a list
    sqliteConnection = sqlite3.connect('students.db3')
    # Connects to database ‘students.db3’ and stores it in variable sqliteConnection.
    cursor = sqliteConnection.cursor()
    # Connects to the database 'students.db3' and allows user to data manipulate anything 
    # inside the database through the temporary workstation, stores it in a variable called cursor.
    sqlite_select_query = """SELECT UUID,Name,Password from TeacherAccounts"""
    # Literal string stored in variable sqlite_select_query, pulls table name TeacherAccounts 
    # and columns of data under the UUID, Name, Password sections.
    cursor.execute(sqlite_select_query)
    # Executes variable string name sqlite_select_query through the cursor.
    records = cursor.fetchall()
    # Pulls all rows of data under the TeacherAccounts table and stores 
    # it as a list under the list records.
    for row in records: # For loop repeats until no more rows of data can be pulled from TeacherAccounts table
    # row is a tuple that stores the data pulled from records.
        teacher = Teacher(row[0],row[1],row[2])
        # teacher is a variable that stores the class data of Teacher.
        # row[0], row[1], row[2] are the 3 elements in the tuple that store the column data UUID, Name, Password 
        # from TeacherAccounts accordingly and applies the data into the object attributes of Teacher.
        teachers.append(teacher)
        # Appends the variable teacher, applies it to the end of the list teachers
    cursor.close
    # Closes the connection to the database
    return teachers
    # Returns the list teachers and the final output of the function get_all_teachers_from_db() is all the teacher’s 
    # uuid, name and password from the TeacherAccount table and is displayed as the list, teachers.

def unit_test():
    teachers = get_all_teachers_from_db()
    assert(len(teachers) > 0)
    
unit_test()