#!/usr/bin/python3
# written by: atholcomb
# anagram.py
# Program identifies if the two strings passed in are anagrams

print("String#1\tString#2\tanagram")

def is_anagram(str_one, str_two):
  str_one = str_one.lower()
  str_two = str_two.lower()
  
  if ''.join(sorted(str_one)) in ''.join(sorted(str_two)):
    return f"{str_one}\t\t{str_two}\t\tTrue"
  else: 
    return f"{str_one}\t\t{str_two}\t\tFalse"


print(is_anagram("Alice", "Bob"))
print(is_anagram("Peter", "Andrew"))
print(is_anagram("Teddy", "Robot"))
print(is_anagram("Angel", "glean"))
print(is_anagram("arc", "car"))
print(is_anagram("bored", "robed"))
print(is_anagram("Listen", "Silent"))
print(is_anagram("hello", "oellh"))
print(is_anagram("typhoon", "opython"))
