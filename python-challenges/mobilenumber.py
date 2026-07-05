#!/usr/bin/python3
# written by: atholcomb
# mobilenumber.py

import random
import time

def getMobileNumber():
    count = 0
    delim = '-'
    number = ""

    while count < 10: 
        random_num = random.choice('0123456789')
        count += 1
        number += random_num
    
    time.sleep(1)
    return f"Formatted: {number[0:3]}{delim}{number[3:6]}{delim}{number[6:]}", "Non-Formatted:", number            


# Ask user for the number of mobile numbers to be generated
ask = int(input("How many mobile numbers would you like generated?: "))
print("Generating mobile numbers.....")
for a in range(ask):
    print(getMobileNumber())
