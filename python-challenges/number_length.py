#!/usr/bin/python3
# written by: atholcomb
# number_length.py
# Creates a function that takes a number <num> and returns its length.

def number_length(num):
  # keep track of the number of digits via count
  count = 0

  # test for zero as the default case, then set count to 1
  if num == 0:
    count = 1
  # else if number > than zero, then apply integer division
  else:
  # while number != 0, apply integer division
    while num != 0:
      num = num // 10
  # keep count of each digit(s)
      count += 1

  # return the count for each case
  return count


print(number_length(10))
print(number_length(5000))
print(number_length(0))
