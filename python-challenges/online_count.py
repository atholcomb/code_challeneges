#!/usr/bin/python3
# written by: atholcomb
# online_count.py
# Write a function named online_count that takes one parameter. 
# The parameter is a dictionary that maps from strings of names to 
# the string "online" or "offline", as seen above.
# Your function should return the number of people who are online.

def online_count(a_dict):
  count = 0

  for k, v in a_dict.items():
    if 'online' in v:
      count += 1
  return count

print(online_count({ "Alice": "online","Bob": "offline","Eve": "online",}))




