#!/usr/bin/python3
# written by: atholcomb
# common_elements.py
# For two given lists, create a new set of values
# from both making sure to only find unique values

def common_elements(list_a, list_b):
  # create a set with only unique values
  result = set()

  # add the correct value to the set
  for item in list_a:
    if item in list_b:
      result.add(item) 

  # convert the set into a list for ouput
  if result == set():
    return f"Original List: {list_a} -> Unique Value(s): Empty Set" 
  return f"Original List: {list_a} -> Unique Value(s): {result}" 

print(common_elements([-1, 3, 4, 6, 7, 9], [1, 3]))
print(common_elements([1, 3, 4, 6, 7, 9], [1, 2, 3, 4, 7, 10]))
print(common_elements([1, 2, 2, 2, 3, 4, 5], [1, 2, 4, 5]))
print(common_elements([1, 2, 3, 4, 5], [10, 12, 13, 15]))
