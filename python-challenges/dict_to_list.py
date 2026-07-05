#!/usr/bin/python3
# written by: atholcomb
# dict_to_list.py
# Write a function that converts a dictionary into a list, where each element represents a key-value pair.

def dict_to_list(some_dict):
    result = []

    for key, value in some_dict.items():
        result.append([key, value])
    
    return result


print(dict_to_list({ 'a': 1, 'b': 2 }))
print(dict_to_list({ 'shrimp': 15, 'tots': 12 }))
print(dict_to_list({}))
