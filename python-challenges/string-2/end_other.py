#!/usr/bin/python3
# written by: atholcomb
# end_other.py

def end_other(a, b):
  a = a.lower()
  b = b.lower()

  if a in b or b in a:
    return True
  return False


print(end_other('Hiabc', 'abc'))
print(end_other('AbC', 'HiaBc'))
print(end_other('abc', 'abXabc'))
