#!/usr/bin/python3
# written by: atholcomb
# majority_vote.py
# Create a function that returns the majority vote in a list. 
# A majority vote is an element that occurs > N/2 times in a list 
# (where N is the length of the list).

def majority_vote(mvlist):
    for vote in mvlist:
        if mvlist.count(vote) > len(mvlist)/2:
            return vote


print(majority_vote(["A", "A", "B"]))   # A
print(majority_vote(["A", "A", "A", "B", "C", "A"]))  # A
print(majority_vote(["A", "B", "B", "A", "C", "C"]))  # None
