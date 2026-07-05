#!/usr/bin/python3
# written by: atholcomb
# vowels.py
# Write a function that recursively returns the number of vowels in a string.
# If it wasn't clear enough already, you should use recursion in your solution.

def vowels(string):
    count = 0

    # idenitfy the number of vowels within the string, add to count variable
    for s in string:
        if s in 'aeiou':
            count += 1

    # if empty string, return "empty string", else return # of vowels in string    
    if string == "":
        return f"{string}, Empty string"
    return f"{string}, {count} vowels"


print(vowels("apple"))
print(vowels("cheesecake"))
print(vowels("bbb"))
print(vowels(""))
