#!/usr/bin/python3
# written by: atholcomb
# check_square_and_cube.py
# Create a function that takes a list of two numbers and checks if the square 
# root of the first number is equal to the cube root of the second number.

import math

def check_square_and_cube(squared_and_cubed_list):
  square_root = math.sqrt(squared_and_cubed_list[0])
  cube_root = round(math.cbrt(squared_and_cubed_list[1]), 1)

  if square_root != cube_root:
    return f"{square_root}, {cube_root} -> False"
  return f"{square_root}, {cube_root} -> True"

print(check_square_and_cube([4, 8]))
print(check_square_and_cube([16, 48])) 
print(check_square_and_cube([9, 27]))
