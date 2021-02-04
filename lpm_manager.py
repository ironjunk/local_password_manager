# File: Helper functions for Local Password Manager
# Author: Aditya Pandit

# ---------- Scope: Packages {Begin} ---------- #

from random import randint, sample
from sqlite3 import connect
from passlib.hash import pbkdf2_sha256

# ---------- Scope: Packages {End} ---------- #

# ---------- Scope: Database {Begin} ---------- #

# func: to create connection to database
def connection():

    conn = connect("C:\\Users\\ironjunk\\AppData\\Local\\local_pass.db")

    return conn

# func: check password to access database
def check_entry(pass_entry):

    conn = connection()
    c = conn.cursor()

    c.execute("select pass from admin limit 1")
    key = c.fetchone()[0]
    conn.close()

    return pbkdf2_sha256.verify(pass_entry, key)

# ---------- Scope: Database {End} ---------- #

# ---------- Scope: Generate {Begin} ---------- #

# func: to generate password
def generate(w = 1, W = 1, d = 1, s = 1):
    
    spcl_char = "#_.@"

    gen = ""

    for i in range(w):
        gen = gen + chr(randint(97,122))

    for i in range(W):
        gen = gen + chr(randint(65,90))

    for i in range(d):
        gen = gen + chr(randint(48,57))

    for i in range(s):
        gen = gen + spcl_char[randint(0,2)]

    return jumble(gen)

# func: to extract parameter values
def separate(value):
    
    return [int(x) for x in value]

# func: to jumble generated password
def jumble(gen):
    
    jumbled = sample(gen, len(gen))
    
    return "".join(jumbled)

# ---------- Scope: Generate {End} ---------- #

# ---------- Scope: Store {Begin} ---------- #
# ---------- Scope: Store {End} ---------- #

# ---------- Scope: Update {Begin} ---------- #
# ---------- Scope: Update {End} ---------- #



# ---------- Start: Management Functions ---------- #

# func: to store the password
def store(conn, ):
    pass

# func: to update the password
def update():
    pass

# func: to fetch password
def fetch():
    pass
# ---------- End: Management Functions ---------- #

if __name__ == "__main__":
    
    print("Error : Not a runnable program. \nNote : Run pass_main.py")


    # value = input("Enter Value: ")
    # w, W, d, s = separate(value)
    
    # pswd = generate(w, W, d, s)
    # print(pswd)