#!/usr/bin/python3
# written by: atholcomb
# duplicate_letters.py
# Given a common phrase, return which words are duplicates 
# if any individual word in the phrase contains duplicate letters.

def duplicate_letters(string):

    result = [] # store duplicates values into list
    original_string = string # perserve input string for the end output
    string = string.split() # seperate the word from the sentence into a list so we can iterate over the letters
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' # use this list of letters to check against the string
    
    for word in string:
        for letter in letters:
            if word.count(letter) > 1:
                result.append(word)

    if result != []:
        return f"{result} are duplicates in ::: {original_string}"
    return f"There are no duplicates in ::: {original_string}"


print(duplicate_letters("Fortune favours the bold."))
print(duplicate_letters("You can lead a horse to water, but you can't make him drink."))
print(duplicate_letters("Look before you leap."))
print(duplicate_letters("An apple a day keeps the doctor away."))
