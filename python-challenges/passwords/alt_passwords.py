#!/usr/bin/python3
# written by: atholcomb
# passwords.py
# Program provides the option to either check your current password 
# or to generate a new one of varied length and complexity
#
# There are two basic functions:
# check_password: which checks the users input (password) and displays information about it
# gen_password: generates a password of the length entered and includes Alphanumeric and Special character complexity
#
# The last block (while block) is a loop that runs to either check or generate a password and exits the program otherwise


# import random module to be able to obtain a random selection of characters
import random

# Define static variables to initialize
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
special = '!@#$%^&*?'

# check_password function checks the user's password and displays information about it
def check_password(password):
    low = 0
    up = 0
    nums = 0
    spec = 0
    for passwd in password:
        if passwd in lower:
            low += 1
        elif passwd in upper:
            up += 1
        elif passwd in numbers:
            nums += 1
        elif passwd in special:
            spec += 1
        else:
            return "Password does not meet requirements or normal convention"

    return f"Your password has the following characteristics:\n{low} lowercase, {up} uppercase, {nums} number(s), {spec} special character(s)"


# gen_password function generates a new password for the length entered with complexity added
def gen_password(length):
    result = ''
    for l in range(length):
        password = random.choice(lower+upper+numbers+special)
        result += password
    return result


# loop that runs to ask for user input - specifically to check or generate a password
while True:
    ask = input("Check password [check], generate pasword [generate], or [exit]: ")
    if ask == 'check':
        password = input("Enter a password: ")
        print(check_password(password))
    elif ask == 'generate':
        length = int(input("Enter password length [1-100]: "))
        if length > 100:
            while length > 100:
                print("Length can only be 1-100")
                length = int(input("Enter password length [1-100]: "))
        print(gen_password(length))
    else:
        print("Quitting...")
        break
