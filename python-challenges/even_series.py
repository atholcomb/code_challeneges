#!/usr/bin/python3
# written by: atholcomb
# even_series.py
# Based on a random number; computes even series from the number if even or skip if odd.

import random

def even_series():
  values = []
  number = random.randrange(100)

  if number % 2 == 0:
    for n in range(1,number):
      if number % n == 0 :
        values.append(n)
  else:
    return f"{number}, is odd -- skipping"

  return number, values

print(even_series())
