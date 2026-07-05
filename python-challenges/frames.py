#!/usr/bin/python3
# written by: atholcomb
# frames.py
# Create a function that returns the number of frames shown in a given number of minutes for a certain FPS.
# FPS stands for "frames per second" and it's the number of frames a computer screen shows every second.

def frames(int1, int2):
  seconds = 60 * int2

  return int1 * seconds


print(frames(1, 1))     # 60
print(frames(10, 1))    # 600
print(frames(10, 25))   # 15000
