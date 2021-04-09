# File: Main file for Local Password Manager
# Author: Aditya Pandit

# ---------- Scope: Packages {Begin} ---------- #

from getpass import getpass
import lpm_manager as mg

# ---------- Scope: Packages {End} ---------- #

# ---------- Scope: Functions {Begin} ---------- #

# func: to setup the program by prompting user to set the master password
def first_setup():

    print("It seems like this is your first time using the program. Kindly follow the instructions to get the program set up.\n")
    
    while True:
        pass_master = input("Set Master Password: ")
        c_pass_master = input("Confirm Master Password: ")

        if pass_master == c_pass_master:
            if mg.store_master_pass(pass_master):
                print("\nThe Master Password has been set successfully!")
                print("\nNote: Kindly save a backup of the Master Password. If the Master Password is lost there is no way to retrieve all of your stored passwords.")
                
            break
        else:
            print("Make sure you enter same Password in both the fields. Please try again.\n")

# ---------- Scope: Functions {End} ---------- #

# ---------- Scope: Main {Begin} ---------- #

if __name__ == "__main__":

    if not mg.check_status():
        first_setup()
    else:
        pass_master = getpass("Enter Master Password: ")
        
        if not mg.check_master_pass(pass_master):
            print("Invalid Password !")
            exit()

# ---------- Scope: Main {End} ---------- #