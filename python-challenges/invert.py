#!/usr/bin/python3
# written by: atholcomb
# invert.py
# Write a function that inverts the keys and values of a dictionary.

def invert(some_dict):
    result = dict()

    for key, value in some_dict.items():
        result[value] = key

    return result

print(invert({ "z": "q", "w": "f" }))
print(invert({ "a": 1, "b": 2, "c": 3 }))
print(invert({ "zebra": "koala", "horse": "camel" }))
