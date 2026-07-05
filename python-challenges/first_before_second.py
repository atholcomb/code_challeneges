#!/usr/bin/python3
# written by: atholcomb
# first_before_second.py
# You are given three inputs: a string, one letter, and a second letter.
# Write a function that returns True if every instance of the first letter occurs before every instance of the second letter.

def first_before_second(string, key1, key2):
    before = []
    after = []

    # obtain positions of key1
    for s1 in range(len(string)):
        if string[s1] in key1:
            before.append(s1)

    # obtain positions of key2
    for s2 in range(len(string)):
        if string[s2] in key2:
            after.append(s2)
    
    # compare positions and return True or False
    for a in after:
        for b in before:
            if a < b:
                return False
    return True


print(first_before_second("a rabbit jumps joyfully", "a", "j"))         # True
print(first_before_second("knaves knew about waterfalls", "k", "w"))    # True
print(first_before_second("happy birthday", "a", "y"))                  # False
print(first_before_second("precarious kangaroos", "k", "a"))            # False
