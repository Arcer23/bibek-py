from controllers import bossController
from controllers import managerController
from config import db
from auth import auth


def add_employee():
    emp_id = input("Employee ID: ")            
    name = input("Name: ")
    department = input("Department: ")
    password = input("Password: ")
    
    db.employees.append(emp_id, name, department, password)
    print("Employee added successfully")

    
def view_employees():
    if not db.employees:
        print("No employees available.")
    else:
        for emp_id, data in db.employees.items():
            print(emp_id, data)

def employee_menu(username):
    while True:
        print("\n--- Employee Menu ---")
        print("1. View Profile")
        print("2. Edit Profile")
        print("3. Reset Password")
        print("4. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            print(db.employees.get(username, "Profile not found"))
        elif choice == "2":
            employeeController.edit_profile(username)
        elif choice == "3":
            employeeController.reset_password(username)
        elif choice == "4":
            break
        else:
            print("Invalid choice!")
    
def edit_profile(username):
    if username in employees:
        new_name = input("Enter new name: ")
        new_dept = input("Enter new department: ")
        db.employees[username]["name"] = new_name
        db.employees[username]["department"] = new_dept
        print("Profile updated successfully!")
    else:
        print("Profile not found!")
    
def reset_password(username):
    new_pass = input("Enter new password: ")
    db.users[username]["password"] = new_pass
    db.employees[username]["password"] = new_pass
    print("Password reset successful!")
