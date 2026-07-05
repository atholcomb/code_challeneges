#!/usr/bin/python3
# written by: atholcomb
# is_disarium.py
# https://edabit.com/challenge/yvJbdkmKHvCNtcZy9

def is_disarium(disarium_number):
  digits = []
  sum_of_digits = 0

  for n in str(disarium_number):
    digits.append(n)

  for index, digit in enumerate(digits, 1):
    sum_of_digits += int(digit) ** index

  if sum_of_digits == disarium_number:
    return True, disarium_number
  else:
    return False, disarium_number, sum_of_digits

print(is_disarium(75))
print(is_disarium(135))
print(is_disarium(544))
print(is_disarium(518))
print(is_disarium(466))
print(is_disarium(8))
