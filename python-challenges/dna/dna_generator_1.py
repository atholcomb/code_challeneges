#!/usr/bin/python3
# written by: atholcomb
# dna_generator_1.py
# dna sequence generator - iteration #1
# Create a DNA sequence from 'atgc' strands

import random
import time

def dna_generator_1():
  dna_strand = 'atgc'

  print("DNA SEQUENCE GENERATOR", "|", "SEQUENCE STARTS IN 3 SECONDS:")
  for t in range(3, 0, -1):
     time.sleep(1)
     print(f"[SEQUENCE START: {t}]")
  for n in range(1, 21):
    print(f"SEQUENCE {str(n).zfill(2)}: ", end='')
    time.sleep(1) 
    for i in range(15):
      choice = random.choice(dna_strand)
      print(choice, end='')
    print(" -> VALIDATED SEQUENCE")

dna_generator_1()
