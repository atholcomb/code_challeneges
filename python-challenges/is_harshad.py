#!/usr/bin/python3
# written by: atholcomb
# is_harshad.py
# A number is said to be Harshad if it's exactly divisible by the sum of its digits. 
# Create a function that determines whether a number is a Harshad or not.

def is_harshad(num):
    sum_list = [] 
    sum_total = 0
    value1 = 0
    value2 = 0
    value3 = 0

    # Seperate numbers into their original digits
    
    if num < 100:
        value1 = num // 10
        value2 = num % 10 
        sum_list.append(value1)
        sum_list.append(value2)
    else:
        value1 = num // 100
        value2 = (num % 100) // 10
        value3 = (num % 100) % 10
        sum_list.append(value1)
        sum_list.append(value2)
        sum_list.append(value3)


    # Calculate sums from sum_list
    
    for sum_value in sum_list:
        sum_total += sum_value

    # Determine if sum_total is a Harshad value or not
    if num % sum_total == 0:
        return True
    return False
    

print(is_harshad(75))   # False
print(is_harshad(171))  # True
print(is_harshad(481))  # True
print(is_harshad(89))   # False
print(is_harshad(516))  # True
print(is_harshad(200))  # True
