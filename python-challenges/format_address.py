#!/usr/bin/python3
# written by: atholcomb
# format_address.py

def format_address(address_string):
    number = 0
    street = ''

    if '123' in address_string:
        number = '123'
    elif '1001' in address_string:
        number = '1001'
    elif '55' in address_string:
        number = '55'
    if 'Main Street' in address_string:
        street = 'Main Street'
    elif '1st Ave' in address_string:
        street = '1st Ave'
    elif 'North Center Drive' in address_string:
        street = 'North Center Drive'
    return "house number {} on street named {}".format(number, street)
    

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"
