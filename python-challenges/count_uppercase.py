#!/usr/bin/python3
# authored by: atholcomb
# count_uppercase.py
# Given random string, return how many uppercase letters there are in a list of various words

def count_uppercase(word_lst):
  count = 0

  for word in word_lst:
    for letter in word:
      # if ord(letter) convert letter into numerical representation
      # range(65, 91) is the numerical representation of A-Z to compare against
      if ord(letter) in range(65, 91):
        count += 1
  return count

print(count_uppercase(["SOLO", "hello", "Tea", "wHat"])) # should be 6
print(count_uppercase(["little", "lower", "down"])) # should be 0 
print(count_uppercase(["EDAbit", "Educate", "Coding"])) # should be 5
