#!/usr/bin/python3
# written by: atholcomb
# check_perfect.py
# Create a function that tests whether or not an integer is a perfect number. 
# A perfect number is a number that can be written as the sum of its factors, excluding the number itself.
# For example, 6 is a perfect number, since 1 + 2 + 3 = 6, where 1, 2, and 3 are all factors of 6. 
# Similarly, 28 is a perfect number, since 1 + 2 + 4 + 7 + 14 = 28.

def check_perfect(number):
  factors = []
  sum_factors = 0

  # obtain the factors and store them into factors list
  for n in range(1, number):
    if number % n == 0:
      factors.append(n)

  # sum the digits of the original number to see if it's perfect
  for factor in factors:
      sum_factors += factor

  if sum_factors == number:
    return True
  return False 


print(check_perfect(6))
print(check_perfect(28))
print(check_perfect(496))
print(check_perfect(12))
print(check_perfect(97))
