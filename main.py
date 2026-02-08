from controllers import bossController
from controllers import employeeController
from controllers import managerController
from config import db
from auth import *

print("\n===== Employee Management System =====\n")
print("1. Boss")
print("2. Manager")
print("3. Employee\n")

role_choice = input("Select role: ")

username, role = auth.login()

if role == "Boss" or role == "boss":
   bossController.boss_menu()
elif role == "Manager" or role=="manager":
    managerController.manager_menu()
elif role == "Employee" or role=="employee":
    employeeController.employee_menu()
else:
    print("Invalid input")

print("\nThank you for using the system.")
