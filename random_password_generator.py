import string 
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_password():
    password_lengt=int(input("how long would you like your password to be ?"))
    random.shuffle(characters)

    password =[]

    for x in range(password_lengt):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)

    print(password)

generate_password()