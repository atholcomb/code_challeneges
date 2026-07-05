#!/usr/bin/python3
# written by: atholcomb
# front_back.py

def front_back(str):
    f = str[:1]
    b = str[-1:]
    m1 = str.index(f)
    m2 = str.index(b)    
    
    return str[m1:m2]


print(front_back('code'))
print(front_back('a'))
print(front_back('ab'))
