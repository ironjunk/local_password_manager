# File: Main file for Local Password Manager
# Author: Aditya Pandit

# ---------- Scope: Packages {Begin} ---------- #

from getpass import getpass
import manager as mg

# ---------- Scope: Packages {End} ---------- #

# ---------- Scope: Functions {Begin} ---------- #
# ---------- Scope: Functions {End} ---------- #

# ---------- Scope: Main {Begin} ---------- #

if __name__ == "__main__":

    pass_entry = getpass("Enter Password: ")
    
    if not mg.check_entry(pass_entry):
        print("Invalid Password !")
        exit()

    

# ---------- Scope: Main {End} ---------- #