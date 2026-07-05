#!/usr/bin/python3
# written by: atholcomb
# secretToHex.py
# For a given secret, convert the secret
# into a hexidecimal representated hash

import random

# header statement for secret and hash
print("Secret\t\tHash")

def secretToHex(secret):
  hex_key = []
  hex_key_choice = ''

  # The range of hexidecimal values to use
  a = 0x0
  b = 0xff
  
  # Append to the list the hexidecimal values
  for x in range(a, b):
    hex_key.append(hex(x))

  # Create a 5 length hexidecimal hash sum
  for c in range(5):
    hex_key_choice += random.choice(hex_key)
 
  # replace the given secret with the hexidecimal hash
  return f"{secret}:\t\t" + secret.replace(secret, hex_key_choice)

print(secretToHex("left"))
print(secretToHex("rhino"))
print(secretToHex("wheel"))
print(secretToHex("word"))
print(secretToHex("beak"))
print(secretToHex("weird"))
print(secretToHex("tower"))
print(secretToHex("ignite"))
print(secretToHex("lazy"))
print(secretToHex("power"))
print(secretToHex("redrum"))
