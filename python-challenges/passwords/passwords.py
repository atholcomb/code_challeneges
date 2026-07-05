#!/usr/bin/python3
# written by: atholcomb
# passwords.py
# Password Module which generates a password of a specified length
# refer to: make_password.py

from random import choice

def generate_passwords(length):
  password = ''

  pswd_char_set = [
  'a','b','c','d','e','f','g','h','i','j','k','l','m',
  'n','o','p','q','r','s','t','u','v','w','x','y','z',
  'A','B','C','D','E','F','G','H','I','J','K','L','M',
  'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
  '%','&','$','#','@','!','*','?','/',
  '1','2','3','4','5','6','7','8','9','0' 
  ]

  for i in range(length):
    password += choice(pswd_char_set)

  return password
