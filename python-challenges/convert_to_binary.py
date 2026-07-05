#!/usr/bin/python3
# written by: atholcomb
# convert_to_binary.py
# Given an integer, return the binary equivalant

def convert_to_binary(integers):
  # header row
  print("Integer\t\tBinary")

  # conversion for each integer into binary
  for integer in integers:
    print(f"{integer}\t\t{bin(integer)[2:]}")

# function call
convert_to_binary([10, 12, 25, 45])
