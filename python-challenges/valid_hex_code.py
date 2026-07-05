#!/usr/bin/python3
# written by: atholcomb
# valid_hex_code.py
# Create a function that determines whether a string is a valid hex code.
# A hex code must begin with a pound key # and is exactly 6 characters in length. 
# Each character must be a digit from 0-9 or an alphabetic character from A-F. 
# All alphabetic characters may be uppercase or lowercase.

def is_valid_hex_code(hex_string):
    lower_hex = hex_string.lower()

    if "#" in lower_hex and len(lower_hex) == 7:
        if "&" in lower_hex or "z" in lower_hex:
            return False
        return True
    else:
        return False


print(is_valid_hex_code("#CD5C5C"))     # True
print(is_valid_hex_code("#EAECEE"))     # True
print(is_valid_hex_code("#eaecee"))     # True
print(is_valid_hex_code("#CD5C58C"))    # False (longer than 7 chars)
print(is_valid_hex_code("#CD5C5Z"))     # False (contains 'z')
print(is_valid_hex_code("#CD5C&C"))     # False (contains '&')
print(is_valid_hex_code("CD5C5C"))      # False (no '#' sign)
