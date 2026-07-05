#!/usr/bin/python3
# written by: atholcomb
# uncensor.py
# Someone has attempted to censor my strings by replacing every vowel with 
# a *, l*k* th*s. Luckily, I've been able to find the vowels that were removed.
# Given a censored string and a string of the censored vowels, return the 
# original uncensored string.

def uncensor(string, vowels):
    # create vowels list to iter over
    char_vowels = []
    for vowel in vowels:
        char_vowels.append(vowel)

    # identify strings with * in them and zip them with vowels
    # print modified string with vowels; else original string
    if '*' in string:
        for r in zip(string.split('*'), char_vowels):
            print(''.join(r), end='')
        print()
    else:
        print(string)


uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo")
uncensor("abcd", "")
uncensor("*PP*RC*S*", "UEAE")
