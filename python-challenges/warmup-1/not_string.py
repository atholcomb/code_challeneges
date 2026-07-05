#!/usr/bin/python3
# written by: atholcomb
# not_string.py

def not_string(str):
    if "not" in str[:3]:
        return str
    else:
        return "not " + str

print(not_string('candy'))
print(not_string('x'))
print(not_string('not bad'))
print(not_string('is not'))
