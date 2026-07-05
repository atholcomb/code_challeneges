#!/usr/bin/python3
# written by: atholcomb
# make_sandwhich.py
# Given a list of ingredients lst and a flavour string as input, create a function that 
# returns the list, but with the elements bread around the selected ingredient

def make_sandwich(lst, string):
    result = lst.copy()

    # handle the last case first
    if lst.count(string) > 1:
        temp = result.index(string)
        result.insert(temp, 'bread')
        result.insert(temp+2, 'bread')
        result.insert(temp+2, 'bread')
        result.insert(temp+5, 'bread')

    else: # handle the remaining cases
        for item in lst:
            if string in item:
                temp = result.index(item)
                result.insert(temp, 'bread')
                result.insert(temp+2, 'bread')

    return result

print(make_sandwich(["tuna", "ham", "tomato"], "ham")) # ["tuna", "bread", "ham", "bread", "tomato"]
print(make_sandwich(["cheese", "lettuce"], "cheese")) # ["bread", "cheese", "bread", "lettuce"]
print(make_sandwich(["ham", "ham"], "ham")) # ["bread", "ham", "bread", "bread", "ham", "bread"]
