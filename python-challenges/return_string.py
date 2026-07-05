#!/usr/bin/python3
# written by: atholcomb
# return_string.py
# return a string when given a list of strings

def return_string(list):
    result = ''

    for item in list:
        result += item + ' '

    return result

print(return_string(["hello", "world"]))
print(return_string(["some", "long", "string"]))
print(return_string(["today's", "date"]))
print(return_string(["sunshine"]))
