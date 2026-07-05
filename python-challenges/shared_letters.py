#!/usr/bin/python3
# written by: atholcomb
# shared_letters.py
# Create a function that returns the number of characters shared between two words

def shared_letters(string1, string2):
    result = 0

    for s1 in string1:
        for s2 in string2:
            if s1 in s2:
                result += 1

    return result   

print(shared_letters("apple", "meaty"))
print(shared_letters("fan", "forsook"))
print(shared_letters("spout", "shout"))
