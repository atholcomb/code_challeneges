#!/usr/bin/python3
# written by: atholcomb
# same_length.py
# Write a function that returns True if every consecutive sequence of ones 
# is followed by a consecutive sequence of zeroes of the same length.

def same_length(seq):
    ones_count = 0
    zeros_count = 0
    for s in seq:
        if '1' in s:
            ones_count += 1
        else:
            zeros_count +=1
    
    if ones_count == zeros_count:
        return True
    return False        

print(same_length("110011100010"))      # True
print(same_length("101010110"))         # False
print(same_length("111100001100"))      # True
print(same_length("111"))               # False
