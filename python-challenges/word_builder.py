#!/usr/bin/python3
# written by: atholcomb
# word_builder.py
# Create a function that builds a word from the scrambled letters contained in the first list. 
# Use the second list to establish each position of the letters in the first list. 
# Return a string from the unscrambled letters (that made-up the word).

def word_builder(letters, indexes):
    word = ''

    for index in indexes:
        word += letters[index]

    return word


print(word_builder(["g", "e", "o"], [1, 0, 2])) # ego
print(word_builder(["e", "t", "s", "t"], [3, 0, 2, 1])) # test
print(word_builder(["b", "e", "t", "i", "d", "a"], [1, 4, 5, 0, 3, 2])) # edabit
