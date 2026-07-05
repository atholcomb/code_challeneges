#!/usr/bin/python3
# written by: atholcomb
# pluralize.py
# Given a list of words in the singular form, return a set of those words in 
# the plural form if they appear more than once in the list.

def pluralize(list_of_words):
    # dict comprehension
    return {plurals+'s'
            if list_of_words.count(plurals) > 1
            else plurals for plurals in sorted(list_of_words)
    }


print(pluralize(["cow", "pig", "cow", "cow"]))
print(pluralize(["table", "table", "table"]))
print(pluralize(["chair", "pencil", "arm"]))
