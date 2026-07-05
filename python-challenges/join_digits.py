#!/usr/bin/python3
# written by: atholcomb
# join_digits.py
# Create a function which takes in a number n as input and returns all numbers up to and 
# including n joined together in a string. Separate each digit from each other with the character "-"

def join_digits(n):
    result = []

    for nums in range(1, n+1):
        result.append(str(nums))

    return '-'.join(result)


print(join_digits(4))
print(join_digits(11))
print(join_digits(15))
