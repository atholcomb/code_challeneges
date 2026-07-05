#!/usr/bin/python3
# written by: atholcomb
# add_str_nums.py
# Write a function that adds two numbers. 
# However, the output has to be strings.

def add_str_nums(a, b=0):
    result = 0
    chars = 'abcdefg'

    if chars in a:
        return f"no value but " + b
    elif a == '' and b == '':
        return "empty"
    elif a == '':
        return b
    elif b == '':
        return a
    else:
        result = int(a) + int(b)

    return str(result)


print(add_str_nums("4", "5"))
print(add_str_nums("abcdefg", "3"))
print(add_str_nums("1", ""))
print(add_str_nums("", ""))
print(add_str_nums("1874682736267235927359283579235789257", "32652983572985729"))
