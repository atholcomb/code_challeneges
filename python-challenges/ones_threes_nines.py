#!/usr/bin/python3
# written by: atholcomb
# ones_threes_nines.py
# Given an int, figure out how many ones, threes and nines you could fit 
# into the number. You must create a class. You will make variables 
# (self.ones, self.threes, self.nines) to do this.

class ones_threes_nines():
  def __init__(self, m):
    self.m = m
    self.ones = 1
    self.threes = 3
    self.nines = 9
  
  def getOnes(self):
    if self.m % self.ones == 0:
      return self.m

  def getThrees(self):
    return self.m // self.threes

  def getNines(self):
    return self.m // self.nines

def main():
  n1 = ones_threes_nines(5)
  print("ones:", n1.getOnes())
  print("threes:", n1.getThrees())
  print("nines:", n1.getNines())

main()
