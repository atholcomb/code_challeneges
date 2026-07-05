#!/usr/bin/python3
# written by: atholcomb
# find_divisors.py
# Given an number, find the divisors for the given number

def find_divisors(n):
    result = []
    
    for num in range(1,n+1):
        if n % num == 0:
            result.append(num)
    
    return f"# {n} has these divisors: {result}"

print(find_divisors(4)) # 4 has 3 divisors: 1, 2 and 4
print(find_divisors(12)) # 12 has 6 divisors: 1, 2, 3, 4, 6, 12
print(find_divisors(25)) # 25 has 3 divisors: 1, 5, 25
