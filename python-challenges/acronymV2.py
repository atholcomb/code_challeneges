#!/usr/bin/python3
# written by: atholcomb
# acronymV2.py

def convert_to_acronym(phrase):
    phrase = phrase.replace(' - ', ' ')
    phrase = phrase.replace('-', ' ')
    
    acronym = phrase.split()

    for i in range(len(acronym)):
        print(acronym[i][0].upper(), end='')
    print() 

convert_to_acronym("Portable Network Graphics")
convert_to_acronym("First In, First Out")
convert_to_acronym("Asynchronous Javascript and XML")
convert_to_acronym("GNU Image Manipulation Program")
convert_to_acronym("Complementary metal-oxide semiconductor")
convert_to_acronym("Something - I made up from thin air")
