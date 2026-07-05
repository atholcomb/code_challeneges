#!/usr/bin/python3
# written by: atholcomb
# sort_by_letter.py
# Write a function that sorts each string in a list by the letter in alphabetic ascending order (a-z).

# pass this function into result (below) to sort the items alphabetically
def myFunc(s):
    characters = 'abcdefghijklmnopqrstuvwxyz'

    for i in s:
        if i in characters:
            return sorted(i)

# main function to determine the order of the strings and return the result
def sort_by_letter(string_list):
    result = []
    characters = 'abcdefghijklmnopqrstuvwxyz'
    key = ''
    
    for item in string_list:
        for char in item:
            if char in characters:
                result.append(item)
                result.sort(key=myFunc) # call myFunc to sort the items in the list
    
    return result


print(sort_by_letter(["932c", "832u32", "2344b"]))
print(sort_by_letter(["99a", "78b", "c2345", "11d"]))
print(sort_by_letter(["572z", "5y5", "304q2"]))
print(sort_by_letter([]))
