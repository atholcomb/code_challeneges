#!/usr/bin/python3
# written by: atholcomb
# find_discount.py
# Create a function that takes two arguments: the original price and the discount
# percentage as integers and returns the final price after the discount.

from random import randint

def main():
  print("1,000's Discount Dollar Amount ($Amt)")
  print("Discount = Per%   $Amt  $Difference")

  for price, discount in generate_values_1000s().items():
    if discount % 10 == discount:
      print(find_discount_1s_place(price, discount))
    elif discount % 100 == discount:
      print(find_discount_2s_place(price, discount))
   
  print("\n100's Discount Dollar Amount ($Amt)")
  print("Discount = Per%   $Amt  $Difference")

  for price, discount in generate_values_100s().items():
    if discount % 10 == discount:
      print(find_discount_1s_place(price, discount))
    elif discount % 100 == discount:
      print(find_discount_2s_place(price, discount))

  print("\n10's Discount Dollar Amount ($Amt)")
  print("Discount = Per%   $Amt $Difference")

  for price, discount in generate_values_10s().items():
    if discount % 10 == discount:
      print(find_discount_1s_place(price, discount))
    elif discount % 100 == discount:
      print(find_discount_10s_place(price, discount))

# generate_values_1000s instantiates a dict of $1000s
def generate_values_1000s():
  values = {}
  for i in range(5):
    price = randint(1000, 10000)
    discount = randint(1, 99)
    values[price] = discount

  return values

# generate_values_100s instantiates a dict of $100s
def generate_values_100s():
  values = {}
  for i in range(5):
    price = randint(100, 1000)
    discount = randint(1, 99)
    values[price] = discount

  return values

# generate_values_10s instantiates a dict of $10s
def generate_values_10s():
  values = {}
  for i in range(5):
    price = randint(10, 100)
    discount = randint(1, 99)
    values[price] = discount

  return values

# find_discount function calls either the 1s place function
# or the 2s place function depending on the discount applied
# or a special case for 10s placeholder column
def find_discount_1s_place(price, discount):
  answer = round(price - ((price * discount) / 100), 2)
  return f"${answer:<7} = .{discount}% of ${price} (${price:>2} - ${((price * discount) / 100)})"

def find_discount_2s_place(price, discount):
  answer = round(price - ((price * discount) / 100), 2)
  return f"${answer:<7} = {discount}% of ${price} (${price:>2} - ${((price * discount) / 100)})"

def find_discount_10s_place(price, discount):
  answer = round(price - ((price * discount) / 100), 2)
  return f"${answer:<7} = {discount}% of ${price} (${price} - ${((price * discount) / 100)})"
 
if __name__ == "__main__":
        main()
