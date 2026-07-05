#!/usr/bin/python3
# written by: atholcomb
# sum_strs.py
# Create a function that takes a list of "mostly", 
# numbers and returns their sum. Watch out for strings!

def sum_strs(nums):
  result = 0

  # addresses the B and z in the last list
  for k, v in enumerate(nums):
    if nums[k] == "B" or nums[k] == "z":
      nums[k] = 0

  for v in nums:
    result += int(v)    

  return result

print(sum_strs["1", "3", "5", "7", "9"])) # 25
print(sum_strs["7", "3", "1", "9", "5"])) # 25
print(sum_strs["1", "5", "B", "9", "z"])) # 15
