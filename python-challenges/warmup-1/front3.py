#!/usr/bin/python3
# written by: atholcomb
# front3.py

def front3(str):
    front3 = str[:3]

    if len(str) < 1:
        return str
    else:
        return front3 * 3


print(front3('Java'))
print(front3('Chocolate'))
print(front3('abc'))
