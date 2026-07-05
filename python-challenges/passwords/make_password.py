#!/usr/bin/python3
# written by: atholcomb
# make_password.py
# Program creates a password and checks the complexity of the password
# Complexity must meet 8 characters length, alpha-numeric, and a special character

from passwords import generate_passwords

def make_password():
  # Set the length of the password to be tested here
  password = generate_passwords(12)

  # check how many times each case is present adding 1 to count
  # if all counts are >=1, then it's a valid password
  lower_count = 0
  upper_count = 0
  symbol_count = 0
  numeral_count = 0

  # cases to be tested 
  lower = "abcdefghijklmnopwrstuvwxyz"
  upper = "ABCDEFGHIJKLMNOPQSRTUVWXYZ"
  symbols = "?*&%$#@!/"
  numerals = "1234567890"

  # conditions applied to cases above
  print("Password:", password)
  for i, p in enumerate(password):
    if password[i] in lower:
      lower_count += 1
    elif password[i] in upper:
      upper_count += 1
    elif password[i] in symbols:
      symbol_count += 1
    elif password[i] in numerals:
      numeral_count += 1

  # return 'valid password' if all criteria are met, otherwise return "not valid password"
  if lower_count >= 1 and upper_count >= 1 and symbol_count >= 1 and numeral_count >= 1:
    return lower_count, upper_count, symbol_count, numeral_count, "valid password"
  return lower_count, upper_count, symbol_count, numeral_count, "not valid password"


print(make_password())
