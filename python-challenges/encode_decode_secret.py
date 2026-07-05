#!/usr/bin/python3
# written by: atholcomb
# encode_decode_secret.py
# encrypts and decrypts a given secret

from random import choice

def encode_decode_secret(secret):
  cipher = ""
  hexidecimal_str = "0123456789ABCDEF"
  
  for key_len in range(15):
    cipher += choice(hexidecimal_str)

  msg = secret

  enc_secret = msg.replace(secret, cipher)

  dec_secret = msg.replace(cipher, msg)

  return f"Msg: {msg:12} Encrypted Msg: {enc_secret:16} Decrypted Msg: {dec_secret}"
  
print(encode_decode_secret("hello world"))
print(encode_decode_secret("left"))
print(encode_decode_secret("rhino"))
print(encode_decode_secret("wheel"))
print(encode_decode_secret("word"))
print(encode_decode_secret("beak"))
print(encode_decode_secret("weird"))
print(encode_decode_secret("tower"))
print(encode_decode_secret("ignite"))
print(encode_decode_secret("lazy"))
print(encode_decode_secret("power"))
print(encode_decode_secret("redrum"))
