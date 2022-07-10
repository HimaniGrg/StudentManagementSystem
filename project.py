import sys
import mysql.connector
from tabulate import tabulate

class Database:
    conn = cursor = None

    def __init__(self):
        global conn, cursor
        #connect to the database
        try:
            conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="student_management_system"
            )
            cursor = conn.cursor()
        
            print("Database is connected sucessfully!")

        except Exception as error:
            print(error)

    # def create_table(self):
    #     sql = "create table Student (Student_id int Primary key auto_increment,Student_name varchar(20),Level varchar(10),Course varchar(50));"
    #     cursor.execute(sql)
    #     print("Table created!")
    
    def __del__(self):
        conn.commit()

class Student(Database):
    
    def accept(self):
        # to add details of a new student
        
        id = int(input("Enter the student_id: "))
        name = input("Enter the name of student: ")
        level = input("Enter the level: ")
        course = input("Enter the course: ")

        query = "INSERT INTO Student(Student_id,Student_name,Level,Course)VALUES({},'{}','{}','{}');".format(id,name,level,course)
        try:
            cursor.execute(query)
            print("New record is added!")

        except Exception as err:
            print(err)
            
        
    def display(self):
        # to display all the records in the table
        query = "SELECT * FROM Student;"
        cursor.execute(query)
        # display all records
        table = cursor.fetchall()
        if table:
        # fetch all columns
            print("List of students:\n")
            print(tabulate(table , headers =["Student_id","Student_name","Level","Course"], tablefmt = "pretty"))
        else:
            print("No data found!")
            
    def search(self,name):
        query = "SELECT * FROM student WHERE student_name like '{}%';".format(name)
        cursor.execute(query)

        table = cursor.fetchall()
        if not table:
            print("\nNo such data!")
        else:
            print("\nFound Data:\n")
            print(tabulate(table , headers =["Student_id","Student_name","Level","Course"], tablefmt = "grid"))


    def update(self,id,field_name,new_value):
        query = "UPDATE student SET {} = '{}' WHERE student_id = {};".format(field_name,new_value,id)
        cursor.execute(query)
        print("A record is updated!")
        spacer()
        st.display()

    def delete(self,id):
        query = "DELETE FROM student WHERE student_id= {}".format(id)
        cursor.execute(query)
        print("A record is deleted!")
        spacer()
        st.display()

def spacer():
    print("_"* 50)

def main():
    running = True
    while running:
        print("""\n****************** SYSTEM MENU *******************
                      1. Display all details of student
                      2. Add details of new student
                      3. Search details of a student
                      4. Update the detail of a student
                      5. Delete the detail of a student
                      6. Exit
                      """)

        choice = int(input("Enter your choice: "))
        spacer()
        if choice == 1:
            st.display()
            spacer()

        elif choice == 2:
            st.accept()
            spacer()

        elif choice ==3:
            name = input("Enter the name of the student: ")
            st.search(name)
            spacer()

        elif choice ==4:
            id = int(input("Enter the id of student: "))
            field_name = input("What do you want to change?")
            new_value = input("Enter the new value: ")
            st.update(id,field_name,new_value)
            spacer()

        elif choice == 5:
            id = int(input("Enter the id of student: "))
            st.delete(id)
            spacer()

        elif choice == 6:
            print("Thank you for your time!")
            running = False
            sys.exit()

        else:
            sys.exit()

print("="*20 + "WELCOME TO STUDENT MANAGEMENT SYSTEM " + "="*20)
db = Database()
st = Student()
if __name__ == "__main__":
    main()
    
