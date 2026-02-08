from controllers import employeeController
from config import db
from auth import auth

def boss_menu():
    while True:
        print("\n--- Boss Menu ---")
        print("1. View all employees")
        print("2.View all employees details")
        print("2. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            if not db.employees:
                print("No employees found.")
            else:
                for emp_id, data in db.employees.items():
                    print(emp_id, data)
        else:
            print("Invalid choice!")


