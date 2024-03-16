#import modules
#https://www.simplifiedpython.net/python-gui-login/
#https://pynative.com/python-sqlite-update-table/
from tkinter import *
from tkinter import ttk
import sqlite3
from src.ReadStudentAccounts import *
from src.ReadTeacherAccounts import *
from src.ViewUpdateExams import *

list_of_subjects = ["English", "Math", "Chinese", "Science"]
list_of_exams = ["CA1", "SA1", "CA2", "SA2"]
# Preloaded sets of lists in the code to allow easy access for functions later in the code.

students = get_all_students_from_db()
teachers = get_all_teachers_from_db()
# Preloaded variables that are lists that contain all the information about students and teachers accounts
# Allow easy access for functions later in the code.


# Picks function, login verification, based on radio button clicked

def log_student_or_teacher():
    val = var.get() 
    print(val)
    if val == 1:
        student_login_verify()
    elif val == 2:
        teacher_login_verify()
        
# Picks function based on what is inputted, subject or student UUID

def subject_or_student_marks():
    global subject_or_student 
    subject_or_student = subject_or_mark.get()
    if any(x in subject_or_student for x in list_of_subjects):
        subject_exam_results()
    for s in students:
        if subject_or_student == s.uuid:
            get_student_marks()
            
# Get all marks of one student stscreen

def get_student_marks_stscreen(): 
    sqliteConnection = sqlite3.connect('students.db3')
    cursor = sqliteConnection.cursor()
    results = []
    for x in list_of_subjects:
        query = "SELECT CA1, SA1, CA2, SA2 FROM " + x + " where StudentUUID = ?"
        cursor.execute(query, (student_uuid,))
        results = cursor.fetchall()
        for result in results:
            tree.insert("", END, values=([x], *result)) 

# Get all marks of one student teacherscreen

def get_student_marks(): # Function has been adapted from https://pynative.com/python-sqlite-select-from-table/
    sqliteConnection = sqlite3.connect('students.db3')
    cursor = sqliteConnection.cursor()
    results = []
    for x in list_of_subjects:
        query = "SELECT CA1, SA1, CA2, SA2 FROM " + x + " where StudentUUID = ?"
        cursor.execute(query, (subject_or_student,))
        results = cursor.fetchall()
        for result in results:
            tree2.insert("", END, values=([x], *result)) 

# Gets all student marks in one subject

def subject_exam_results():
    sqliteConnection = sqlite3.connect('students.db3')
    cursor = sqliteConnection.cursor()
    sqlite_select_query = "SELECT * from " + subject_or_student
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    for row in records:
        tree2.insert("", END, values=row)
    sqliteConnection.close()


# Used to check username_verify and password_verify if they are a student
# and identify if the login credentials exist in the database.

def student_login_verify(): 
    global student_name 
    global student_uuid 
    username1 = username_verify.get()
    password1 = password_verify.get()
    student = None
    for s in students:
        if username1 == s.uuid:
            student = s
    if not student == None:
        if password1 == student.password:
            student_name = student.name
            student_uuid = student.uuid
            student_screen()
        else:
            password_not_recognised()
    else:
        user_not_found()
    
# Used to check username_verify and password_verify if they are a teacher
# and identify if the login credentials exist in the database.

def teacher_login_verify(): 
    global teacher_name 
    username1 = username_verify.get()
    password1 = password_verify.get()
    teacher = None
    for t in teachers:
        if username1 == t.uuid:
            teacher = t
    if not teacher == None:
        if password1 == teacher.password:
            teacher_name = teacher.name
            teacher_screen()
        else:
            password_not_recognised()
    else:
        user_not_found()       

# Update all marks of one student in one subject into the database.

def update_marks(): 
    uuid = UUID_Update.get()
    subject = Subject_Update.get()
    student = None
    ca1 = CA1_marks.get()
    sa1 = SA1_marks.get()
    ca2 = CA2_marks.get()
    sa2 = SA2_marks.get()

    if ca1 and sa1 and ca2 and sa2 in range(0,101):
        if subject in list_of_subjects:
            for s in students:
                if uuid == s.uuid:
                    student = s
                    update_multiple_columns(uuid, subject, ca1, sa1, ca2, sa2)
                    update_successful()
            if not student == None:
                return 
            else:
                user_not_found()
        else:   
             subject_not_found()
    else:
        marks_not_found()

#set conditions for update, marks can only be from 1-100, uuid and subject must be a student and subject from the database      
     
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen 
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command = delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found(): 
    global user_not_found_screen 
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text = "User Not Found").pack()
    Button(user_not_found_screen, text = "OK", command = delete_user_not_found_screen).pack()
    

# Designing popup for subject not found

def subject_not_found():
    global subject_not_found_screen
    subject_not_found_screen = Toplevel(updatemarksscreen)
    subject_not_found_screen.title("")
    subject_not_found_screen.geometry("150x100")
    Label(subject_not_found_screen, text = "Unknown Subject").pack()
    Button(subject_not_found_screen, text = "OK", command = delete_subject_not_found_screen).pack()

# Designing popup for subject not found

def marks_not_found():
    global marks_not_found_screen
    marks_not_found_screen = Toplevel(updatemarksscreen)
    marks_not_found_screen.title("")
    marks_not_found_screen.geometry("150x100")
    Label(marks_not_found_screen, text = "Marks not within 1-100").pack()
    Button(marks_not_found_screen, text = "OK", command = delete_marks_not_found_screen).pack()

# Designing popup for marks being successfully updated

def update_successful():
    global update_successful_screen
    update_successful_screen = Toplevel(updatemarksscreen)
    update_successful_screen.title("")
    update_successful_screen.geometry("150x100")
    Label(update_successful_screen, text = "Update Successful").pack()
    Button(update_successful_screen, text = "OK", command = delete_update_successful_screen).pack()
    
# Designing Log out Button

def log_out():
    main_screen.update()
    main_screen.deiconify()
    login_screen.destroy()

# Designing clear all TreeView Button
def clear_Tree():
    for row in tree.get_children():
        tree.delete(row)
    # Runs a for loop and it deletes all rows of displayed tree data on the stscreen.
        
def clear_Tree2():
    for row in tree2.get_children():
        tree2.delete(row)    
    # Runs a for loop and it deletes all rows of displayed tree data on the teacherscreen.    

# Deleting popups
 
def delete_password_not_recognised(): 
    password_not_recog_screen.destroy()
 
def delete_user_not_found_screen(): 
    user_not_found_screen.destroy()

def delete_subject_not_found_screen():
    subject_not_found_screen.destroy()
    
def delete_marks_not_found_screen():
    marks_not_found_screen.destroy()

def delete_update_successful_screen():
    update_successful_screen.destroy()
    
# Designing Main(first) window
 
def main_account_screen():
    global main_screen 
    global var 
    main_screen = Tk()
    var = IntVar()
    var.set(1)
    main_screen.geometry("350x200")
    main_screen.title("Account Login")
    Label(main_screen, text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Radiobutton(main_screen, text="Student", variable = var, value = 1).pack(anchor = NW)
    Radiobutton(main_screen, text="Teacher", variable = var, value = 2).pack(anchor = NW)
    Button(main_screen, text = "Login", height = "2", width = "30", command = login).pack()
    main_screen.mainloop()

# Designing window for login 
 
def login(): 
    global login_screen 
    main_screen.withdraw()
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    global username_verify
    global password_verify
    username_verify = StringVar()
    password_verify = StringVar()
    Label(login_screen, text="Username * ").pack()
    Entry(login_screen, textvariable = username_verify).pack()
    Label(login_screen, text="Password * ").pack()
    Entry(login_screen, textvariable = password_verify, show= "*").pack()
    Button(login_screen, text="Login", width=10, height=1, command = log_student_or_teacher).pack()

# Designing Student Screen
 
def student_screen():
    global stscreen 
    global tree
    login_screen.withdraw()
    stscreen = Toplevel(login_screen)
    stscreen.geometry("600x400")
    stscreen.title("Welcome, " + student_name)
    Button(stscreen, text="Log Out", padx=3, pady=3, command=log_out, fg="white", bg="red").pack(anchor = NE)
    tree = ttk.Treeview(stscreen, column=("c1", "c2", "c3", "c4", "c5"), show='headings')
    tree.column("#1", minwidth=0, width=70, anchor=CENTER, stretch=NO)
    tree.heading("#1", text = student_name)
    for (i,subject) in enumerate(list_of_exams):
        tree.column("#"+str(i+2), minwidth=0, width=40, anchor=CENTER, stretch=NO)
        tree.heading("#"+str(i+2), text = subject)
    tree.pack()
    Button(stscreen, text="Display Marks", command=get_student_marks_stscreen).pack(pady=10)
    Button(stscreen, text="Clear data", command = clear_Tree).pack(pady=10)

# Designing Teacher Screen

def teacher_screen():
    global teacherscreen 
    global subject_or_mark 
    global tree2 
    login_screen.withdraw()
    teacherscreen = Toplevel(login_screen)
    teacherscreen.geometry("400x600")
    teacherscreen.title("Welcome, " + teacher_name)
    subject_or_mark = StringVar()
    Button(teacherscreen, text="Log Out", padx=3, pady=3, command=log_out, fg="white", bg="red").pack(anchor = NE)
    Label(teacherscreen, text="View Subject or Student * ").pack()
    Entry(teacherscreen, textvariable = subject_or_mark).pack()   
    tree2 = ttk.Treeview(teacherscreen, column=("c1", "c2", "c3", "c4", "c5"), show='headings')
    tree2.column("#1", minwidth=0, width=70, anchor=CENTER, stretch=NO)
    tree2.heading("#1", text= "")
    for (i,subject) in enumerate(list_of_exams):
        tree2.column("#"+str(i+2), minwidth=0, width=40, anchor=CENTER, stretch=NO)
        tree2.heading("#"+str(i+2), text = subject)
    tree2.pack()
    Button(teacherscreen, text="Display data", command=subject_or_student_marks).pack(pady=10)
    Button(teacherscreen, text="Clear data", command = clear_Tree2).pack(pady=10)
    Button(teacherscreen, text="Update marks", command = update_marks_screen).pack(pady=10)

# Obtain entries to update marks in database

def update_marks_screen():
    global updatemarksscreen 
    global UUID_Update 
    global Subject_Update 
    global CA1_marks 
    global SA1_marks 
    global CA2_marks 
    global SA2_marks
    updatemarksscreen = Toplevel(teacherscreen)    
    updatemarksscreen.geometry("400x300")
    updatemarksscreen.title("Update marks here")
    UUID_Update = StringVar()
    Subject_Update = StringVar()
    CA1_marks = IntVar()
    SA1_marks = IntVar()
    CA2_marks = IntVar()
    SA2_marks = IntVar()

    Label(updatemarksscreen, text="Student ID * ").pack()
    Entry(updatemarksscreen, textvariable = UUID_Update).pack()
    Label(updatemarksscreen, text="Subject * ").pack()
    Entry(updatemarksscreen, textvariable = Subject_Update).pack()
    Label(updatemarksscreen, text="CA1 * ").pack()
    Entry(updatemarksscreen, textvariable = CA1_marks).pack()
    Label(updatemarksscreen, text="SA1 * ").pack()
    Entry(updatemarksscreen, textvariable = SA1_marks).pack()
    Label(updatemarksscreen, text="CA2 * ").pack()
    Entry(updatemarksscreen, textvariable = CA2_marks).pack()
    Label(updatemarksscreen, text="SA2 * ").pack()
    Entry(updatemarksscreen, textvariable = SA2_marks).pack()
    Button(updatemarksscreen, text="Update Marks", width= 10, height= 1, command = update_marks).pack()  
    

main_account_screen()


# Need to update marks for teacher screen
# Need to display overall weightage score from 4 exams
