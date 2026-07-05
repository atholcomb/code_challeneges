#!/usr/bin/python3
# written by: atholcomb
# unstretch.py
# Write a function that takes a string, and returns a new string 
# with any duplicate consecutive letters removed.

def unstretch(string):
    
    return ''.join(dict.fromkeys(string))
        
print(unstretch("ppoeemm")) # poem
print(unstretch("wiiiinnnnd")) # wind
print(unstretch("ttiiitllleeee")) # title
print(unstretch("cccccaaarrrbbonnnnn")) # carbon
