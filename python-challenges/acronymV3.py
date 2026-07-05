#!/usr/bin/python3
# written by: atholcomb
# acronymV3.py

def convert_to_acronym(string):
    string = string.replace(' - ', ' ')
    string = string.replace('-', ' ')
    
    acronym_in_list = string.split()
    print(acronym_in_list)

    acronym = ''
    for i in range(len(acronym_in_list)):
        acronym += acronym_in_list[i][0].upper()
    return acronym


print(convert_to_acronym("Portable Network Graphics"))
print(convert_to_acronym("First In, First Out"))
print(convert_to_acronym("Asynchronous Javascript and XML"))
print(convert_to_acronym("GNU Image Manipulation Program"))
print(convert_to_acronym("Complementary metal-oxide semiconductor"))
print(convert_to_acronym("Something - I made up from thin air"))
