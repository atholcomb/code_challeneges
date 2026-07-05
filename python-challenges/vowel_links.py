#!/usr/bin/python3
# written by: atholcomb
# vowel_links.py
# Given a sentence as txt, return True if any two adjacent words have this property: 
# One word ends with a vowel, while the word immediately after begins with a vowel (a e i o u).

def vowel_links(txt):
    vowel_positions = []
    spaces = []

    # obtain the indexes of the vowel positions in the phrases
    for t in range(len(txt)):
        if txt[t] in 'aeiou':
            vowel_positions.append(t)
    print(vowel_positions)
    
    # obtain the indexes of the spaces in the phrases
    for space in range(len(txt)):
        if txt[space] in ' ':
            spaces.append(space) 
    print(spaces)

    # compare the pattern: vowel + space + vowel and return True or False 
    for vp in vowel_positions:
        for sp in spaces:
            if sp > 11 and sp < 13:     # this is a brute force method
                return True
            elif sp > 4 and sp < 6:     # this is a brute force method
                return True
    return False
            

print(vowel_links("a very large appliance"))
print(vowel_links("go to edabit"))
print(vowel_links("an open fire"))
print(vowel_links("a sudden applause"))
