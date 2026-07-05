#!/usr/bin/python3
# written by: atholcomb
# consec_numbers.py
# Create a function that determines whether elements in an array can be 
# re-arranged to form a consecutive list of numbers where each number 
# appears exactly once.

def consec_numbers(elements):
  for num in elements:
    if elements[::-1] > elements[0:]:
        return False
    else:
        return sorted(elements) 

print(consec_numbers([5, 1, 4, 3, 2])) # [1, 2, 3, 4, 5]
print(consec_numbers([5, 1, 4, 3, 2, 8])) # False
print(consec_numbers([5, 6, 7, 8, 9, 9])) # False
