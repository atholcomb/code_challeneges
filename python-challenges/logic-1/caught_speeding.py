#!/usr/bin/python3
# written by: atholcomb
# caught_speeding.py
# Program should return True if speed is above 60
# and False otherwise with also an exception of a birthday

def caught_speeding(speed, is_birthday):
  if speed <= 60 and is_birthday == True:
    return True
  elif speed <= 60 and is_birthday == False:
    return True
  elif speed > 60 and speed <= 80 and is_birthday == True:
    return True
  else:
    return False


print(caught_speeding(60, True))
print(caught_speeding(65, False))
print(caught_speeding(65, True))
print(caught_speeding(85, True))
