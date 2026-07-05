#!/usr/bin/python3
# written by: atholcomb
# dictionary_formatter.py
# Given a dictionary with another dictionary inside, 
# format the result to the following:
# dict1 = {"a": 1, "b": 2, "c_d": 3, "c_e": 4}

dict1 = {"a": 1, "b": 2, "c": {"d": 3, "e": 4}}

for k, v in list(dict1.items()):
  new = {}
  if 'c' in k:
    for key, item in v.items():
      new[k+'_'+key] = item
      dict1.update(new)
  if 'c' in k:
    dict1.pop('c')

print(dict1)
