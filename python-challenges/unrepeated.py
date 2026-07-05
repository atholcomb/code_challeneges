#!/usr/bin/python3
# written by: atholcomb
# unrepeated.py
# Create a function that will remove any repeated charcter(s) in a word passed to the function

def unrepeated(s):
  return ''.join(sorted(set(s), key=s.index))
    
print(unrepeated("hello"))
print(unrepeated("aaaaa"))
print(unrepeated("WWE!!!"))
print(unrepeated("call 911"))
