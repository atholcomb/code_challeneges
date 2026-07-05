#!/usr/bin/python3
# written by: atholcomb
# combine_lists.py
# Generate a new list containing the elements of list2
# followed by the elements of list1 in reverse order

def combine_lists(list1, list2):
  print("Original Order:", list1 + list2)
  return f"Reversed Order: {list1[::-1] + list2}"
	
print(combine_lists(["Alice", "Cindy", "Bobby", "Jan", "Peter"], ["Mike", "Carol", "Greg", "Marcia"]))
