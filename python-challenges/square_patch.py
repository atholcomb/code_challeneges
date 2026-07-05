#!/usr/bin/python3
# written by: atholcomb
# square_patch.py
# Create a function that takes an integer and outputs an n x n square solely consisting of the integer n.

import math

def square_patch(patch_value):
    patch_list = []
    
    if patch_value == 0:
        return "[]"
    else:
        for pv in range(patch_value):
            patch_list.append(patch_value)

            
    return f"{patch_list}\n" * patch_value 


print(square_patch(3))
print(square_patch(5))
print(square_patch(1))
print(square_patch(0))

# example output
#square_patch(3) [
#  [3, 3, 3],
#  [3, 3, 3],
#  [3, 3, 3]
#]
