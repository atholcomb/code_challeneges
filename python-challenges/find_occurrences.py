#!/usr/bin/python3
# written by: atholcomb
# find_occurrences.py

def findOccurrences(string, key):
    result = dict()
    
    string = string.lower()
    key = key.lower()
    string = string.split() # seperate the word from the sentence into a list
    
    for word in string:
        if key in word:
            result[word] = word.count(key)
        else:
            result[word] = 0

    return result


print(findOccurrences("Hello World", "o"))
print(findOccurrences("Create a nice JUICY function", "c"))
print(findOccurrences("An APPLE a day keeps an Archeologist AWAY...", "A"))
