#!/usr/bin/python3
# written by: atholcomb
# consecutive_combo.py
# Write a function that returns True if two lists, when combined, form a consecutive sequence.

def consecutive_combo(lst1, lst2):
  lst1.extend(lst2)
  sorted_list = sorted(lst1)
  list_length = len(sorted_list)
  original_numbers = list('123456789')
  compare_list = []

  for val in range(1, len(sorted_list)+1):
    for item in original_numbers:
      compare_list.append(int(item))
      if int(item) < list_length+1 and sorted_list == compare_list:
          return True
    return False
        
print(consecutive_combo([7, 4, 5, 1], [2, 3, 6])) # True
print(consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9])) # False
print(consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10])) # False
