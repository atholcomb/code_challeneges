#!/usr/bin/python3
# written by: atholcomb
# Create a function that takes a list containing nested lists as an argument. 
# Each sublist has 2 elements. The first element is the numerator and the second 
# element is the denominator. Return the sum of the fractions rounded to the 
# nearest whole number.

def sum_fractions(nested_lists):
  result = []
  answer = 0

  # divide the numerator by the denominator and store into result
  # divide the first position by the second
  for items in nested_lists:
    result.append(items[0] / items[1])
 
  # add the values from result for a total value
  for res in result:
    answer += res

  # convert answer to an int, leaving off decimal places
  return int(answer)

print(sum_fractions([[18, 13], [4, 5]]))  # 2
print(sum_fractions([[36, 4], [22, 60]])) # 9
print(sum_fractions([[11, 2], [3, 4], [5, 4], [21, 11], [12, 6]]))  # 11
