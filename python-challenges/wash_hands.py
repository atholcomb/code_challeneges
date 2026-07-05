#!/usr/bin/python3
# written by: atholcomb
# It takes 21 seconds to wash your hands and help prevent the spread of COVID-19.
# Create a function that takes the number of times a person washes their hands per day (n)
# and the number of months they follow this routine nM and calculates the duration in
# minutes and seconds that person spends washing their hands.

def wash_hands(n, m):
  time = (n * m * 30 * 21)
  minutes = time / 60
  remainder = minutes % 1

  if remainder == 0.0:
    remainder = 0
  elif remainder == 0.5:
    remainder = 30

  return f"{time} seconds -> {int(minutes)} minutes and {remainder} seconds"

print(wash_hands(8, 7))
print(wash_hands(0, 0))
print(wash_hands(7, 9))
