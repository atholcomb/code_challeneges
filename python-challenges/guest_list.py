#!/usr/bin/python3
# written by: atholcomb
# guest_list.py
# Suppose you have a guest list of students and the country they are from, 
# stored as key-value pairs in a dictionary. Return the name and the country
# that the user is from otherwise, return 'I'm a guest'

GUEST_LIST = {
"Randy": "Germany",
"Karla": "France",
"Wendy": "Japan",
"Norman": "England",
"Sam": "Argentina"
}

def greeting(name):
    if name in GUEST_LIST:
        return f"Hi! I'm {name}, and I'm from {GUEST_LIST[name]}"
    else:
        return "Hi! I'm a guest."


print(greeting('Randy'))
print(greeting('Sam'))
print(greeting('Monti'))
