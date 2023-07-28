from database import *
from utils import *


def admin_menu():
    print("Welcome to Online Courses 📕")
    print("\n 1.Add course 🆕  ||   2.Show students 👨‍🎓👩‍🎓 ")
    answer = int(input("Enter: "))
    if answer == 1:
        add_course()
    elif answer == 2:
        pass
    else:
        print("Try again !")
        admin_menu()

def user_menu(username):
    print("Welcome to Online Courses 📕")
    print("\n 1.Show courses 🆕  ||   2.Join courses  || 3.Show my courses ")
    answer = int(input("Enter: "))
    if answer == 1:
        pass
    elif answer == 2:
        show_courses()
        id = int(input("Enter course id:"))
        join_course(username,id)
    elif answer == 3:
        pass
    else:
        print("Try again !")
        user_menu(username)



def menu():
    print("Welcome to Online Courses 📕")
    print("\n 1.Register 🆕  ||   2.Log in 🔑 ")
    answer = int(input("Enter: "))
    if answer == 1:
       is_exists()
    elif answer == 2:
        username = input("Username: ")
        password=input("Password: ")
        login1 = login(username,password)
        if login1 == 1:
            admin_menu()
        elif login1 == 2:
            user_menu(username)

        
menu()
    