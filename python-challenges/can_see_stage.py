#!/usr/bin/python3
# written by: atholcomb
# can_see_stage.py
# Create a function that determines whether each seat can "see" the front-stage. 
# A number can "see" the front-stage if it is strictly greater than the number 
# before it.

def can_see_stage(seats):
  for idx, row in enumerate(seats):
  # determine if elements in columns are greater than the # before it
    if seats[idx-1][0] > seats[idx-2][0] > seats[idx-3][0]:
      if seats[idx-1][1] > seats[idx-2][1] > seats[idx-3][1]:
        if seats[idx-1][2] > seats[idx-2][2] > seats[idx-3][2]:
          return True
    return False

# True
print(can_see_stage([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]))

# True
print(can_see_stage([
  [0, 0, 0],
  [1, 1, 1],
  [2, 2, 2]
]))

# False
print(can_see_stage([
  [2, 0, 0], 
  [1, 1, 1], 
  [2, 2, 2]
]))

# False
print(can_see_stage([
  [1, 0, 0],
  [1, 1, 1],
  [2, 2, 2]
]))
