#!/usr/bin/python3
# written by: atholcomb
# multi_function_call.py
# Program calls multiple functions and returns
# the evens and odds from a given number list

import random
import json

# return a jsonified version of evens and odds
def find_evens_odds(num_list):
  numbers = {}

  for number in num_list:
    if number % 2 == 0:
      numbers[number] = "even"
    else:
      numbers[number] = "odd"

  return json.dumps(numbers, indent=2)

# input list for first function
def nums():
  num_list = []

  for i in range(10):
    num = random.randint(1, 99)
    num_list.append(num)
   
  return num_list


if __name__ == "__main__":
    print(find_evens_odds(nums()))
