#!/usr/bin/python3
# written by: atholcomb
# win_round.py
# You have a pack of 5 randomly numbered cards, which can range from 0-9. 
# You can win if you can produce a higher two-digit number from your cards, than your opponent. 
# Return True if your cards win that round.

def win_round(card1, card2):
    
    # sort the numbers in reverse order
    c1 = sorted(card1, reverse=True)
    c2 = sorted(card2, reverse=True)

    your_str = ''
    oppon_str = ''

    # obtain the 2 highest digits in string format - for your card
    for c_1 in c1[:2]:
        your_str += str(c_1) 

    # obtain the 2 highest digits in string format - for opponents card
    for c_2 in c2[:2]:
        oppon_str += str(c_2) 

    if int(your_str) > int(oppon_str):
        return f"True, card1: {your_str}, card2: {oppon_str}"
    return f"False, card1: {your_str}, card2: {oppon_str}"


print(win_round([2, 5, 2, 6, 9], [3, 7, 3, 1, 2])) # True
print(win_round([1, 2, 3, 4, 5], [9, 8, 7, 6, 5])) # False
print(win_round([4, 3, 4, 4, 5], [3, 2, 5, 4, 1])) # False
