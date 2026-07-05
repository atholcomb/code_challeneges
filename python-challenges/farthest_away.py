#!/usr/bin/python3
# written by: atholcomb
# farthest_away.py
# Write a program that computes the correct number 
# that is farthest away from three distinct numbers

def farthest_away(numbers):
  largest = max(numbers)
  smallest = min(numbers)

  for num in numbers:
    if num != largest and num != smallest:
      if abs(largest - num) > abs(smallest - num):
        return f'largest: {largest} \tsmallest {smallest} \tfarthest_from_num {num} \tfurthest away: {largest} \tby {abs(largest - num)}'
      else:
        return f'largest: {largest} \tsmallest {smallest} \tfarthest_from_num {num} \tfurthest away: {smallest} \tby {abs(smallest - num)}'
  
print(farthest_away([10, 5, 9]))
print(farthest_away([17, 2, 20]))
print(farthest_away([25, 5, 11]))
print(farthest_away([19, 8, 4]))
