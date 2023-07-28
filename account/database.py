import sqlite3
from datetime import datetime
from utils import *
from tabulate import tabulate



def con():
    return sqlite3.connect('dbt.db')
    

def create_table_user():
    conn = con()
    cur = conn.cursor()
    query = """
            create table users(
                userID integer not null primary key autoincrement,
                first_name varchar(30),
                last_name varchar(30),
                birth_day varchar(10),
                phone varchar(13),
                username varchar(50),
                password varchar(150),
                is_admin boolean default false
            )
        """
    cur.execute(query)
    conn.commit()
    conn.close()



def write_user(data:dict):
    conn = con()
    cur = conn.cursor()
    data['password'] = hash_password(data['password'])
    value = tuple(data.values())
    cur.execute("""
            insert into users(
                first_name,
                last_name,
                birth_day,
                phone,
                username,
                password
            )
            values(?,?,?,?,?,?)
        """,value)
    
    conn.commit()
    conn.close()
        

def check_user(username:str,phone:str):
    conn = con()
    cur = conn.cursor()
    cur.execute("""
        select count(userID) from users
        where username=? and phone=?
        """, (username, phone))
    user_data = cur.fetchone()
    return user_data[0]


        
def is_exists():
    first_name = input("First name: ")
    last_name = input("Last name: ")
    birth_day = input("Birth day[yyyy-mm-dd]: ")
    phone= input("Phone number: ")
    username = input("Username: ")
    password=input("Password: ")
    phone_data = check_phone(phone)
    brith = check_date(birth_day)
    if phone_data and brith:
        user_data = check_user(username,phone)
        if user_data:
            print("This user already exists ❌")
        else:
            data = dict(
                first_name = first_name,
                last_name = last_name,
                birth_day = birth_day,
                phone= phone,
                username= username,
                password=password
                 )
            write_user(data)
            print("Data saved successfully 🟢")
    else:
        print("Error")




def login(username,password):
    conn = con()
    cur = conn.cursor()
    cur.execute("""
        select count(userID) from users
        where username=? and password=?
        """,(username,hash_password(password)))
    user_data = cur.fetchone()
    if user_data:
        cur.execute("""
            select count(is_admin) from users
            where username=? and password=?
        """,(username,hash_password(password)))
    user_data2 = cur.fetchone()
    if user_data2:
        return 1
    else:
        return 2

def create_course_table():
    conn = con()
    cur = conn.cursor()
    cur.execute("""
        create table courses(
            courseID integer not null primary key autoincrement,
            name varchar(50),
            number_of_students int,
            is_active boolean default true
        )
    """)
    conn.commit()
    conn.close()

def check_course(name):
    conn = con()
    cur = conn.cursor()
    cur.execute("""
        select count(courseID) from courses
        where name =?
    """,(name,))
    course = cur.fetchone()
    conn.close()
    return course[0]


def add_course():
    course_name = input('Course name:')
    num_students = int(input('Number of Students:'))
    conn = con()
    cur = conn.cursor()
    check = check_course(course_name)
    if check:
        print("This course already exists ❌")
    else:
        cur.execute("""
        insert into courses(
            name,
            number_of_students
        )
        values
        (?,?)
    """,(course_name,num_students))
        conn.commit()
        print("Course saved 🟢")

def student_course_table():
    conn = con()
    cur = conn.cursor()
    cur.execute("""
        create table mycourse(
            courseID integer not null primary key autoincrement,
            course_id integer, 
            student_id integer,
            join_time datetime,
            foreign key(course_id)
            references users(id),
            foreign key(student_id)
            references music(id)
            
        )
    """)
    conn.commit()
    conn.close()

def show_courses():
    conn = con()
    cur = conn.cursor()
    cur.execute("""
        select * from courses
    """)
    course = cur.fetchall()
    courses = list()
    for i in course:
        courses.append({'Id':i[0],'Name':i[1],'Free place':i[2]})
    conn.close()
    print(tabulate(courses,headers='keys',floatfmt='fancy_grid'))



def join_course(username,id):
    pass






        


    
