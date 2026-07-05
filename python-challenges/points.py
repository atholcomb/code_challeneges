#!/usr/bin/python3
# written by: atholcomb
# points.py
# You are counting points for a basketball game, given the amount of 3-pointers scored and 2-pointers scored, 
# find the final points for the team and return that value ([2 -pointers scored, 3-pointers scored]).

def points(int1, int2):
    two_pointers = 2
    three_pointers = 3

    return (int1 * two_pointers) + (int2 * three_pointers)


print(points(1, 1))     # 5
print(points(7, 5))     # 29
print(points(38, 8))    # 100
