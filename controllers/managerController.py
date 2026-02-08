from controllers import bossController
from controllers import employeeController
from config import db
from auth import auth 

def manager_menu():
    while True:
        print("\n--- Manager Menu ---")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            employeeController.add_employee()
        elif choice == "2":
            employeeController.view_employees()
        elif choice == "3":
            break
        else:
            print("Invalid choice!")
