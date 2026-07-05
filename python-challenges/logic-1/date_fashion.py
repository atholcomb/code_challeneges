#!/usr/bin/python3
# written by: atholcomb
# date_fashion.py

def date_fashion(you, date):
  if you >= 8 and date < 3:
    return 0
  elif date >= 8 and you < 3:
    return 0
  elif you >= 8 or date >= 8:
    return 2
  elif you < 3 or date < 3:
    return 0
  else:
    return 1


print(date_fashion(5, 10))
print(date_fashion(5, 2))
print(date_fashion(5, 5))
print(date_fashion(10, 2))
