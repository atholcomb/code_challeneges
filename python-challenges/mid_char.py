#!/usr/bin/python3
# written by: atholcomb
# mid_char.py
# Your function should extract and return the middle letter. 
# If there is no middle letter, your function should return the empty string.

def mid(string):
    if len(string) % 2 != 0:
      return string[int(len(string) / 2)]
    return ''

print(mid(''))        # empty
print(mid('abc'))     # b
print(mid('abcd'))    # empty
print(mid('abcde'))   # c
print(mid('aaaa'))    # empty
