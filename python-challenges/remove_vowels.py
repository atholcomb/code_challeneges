#!/usr/bin/python3
# written by: atholcomb
# remove_vowels.py
# Write a function that removes all vowels from a string

def remove_vowels(string):
    vowels = 'aeiou'

    for vowel in vowels:
        if vowel in string:
            string = string.replace(vowel, '')

    return string

print(remove_vowels("ben")) # bn
print(remove_vowels("hello")) # hll
print(remove_vowels("apple")) # ppl
