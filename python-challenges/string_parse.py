#!/usr/bin/python3
# written by: atholcomb
# string_parse.py

import re

def parse_code(string):
    new_string = dict() 
    
    ns = re.sub("[0]", ' ', string)
    new = ns.split()

    for item in range(len(new)):
        new_string["first_name"] = new[0]
        new_string["last_name"] = new[1]
        new_string["id"] = new[2]

    return new_string

    
print(parse_code("John000Doe000123"))
print(parse_code("michael0smith004331"))
print(parse_code("Thomas00LEE0000043"))
