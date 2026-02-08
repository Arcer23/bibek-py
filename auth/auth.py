from controllers import bossController
from config import db
from auth import *
        
def login():
    attempts = 0
    while attempts < 3:
        username = input("Username: ")
        password = input("Password: ")

        if username in db.users and db.users[username]["password"] == password:
            print("\nLogin successful!\n")
            return username, db.users[username]["role"]
        else:
            attempts += 1
            print(f"Invalid credentials! Attempts left: {3 - attempts}")

    print("\nToo many failed attempts. System terminated.")
    exit()
