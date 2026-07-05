#!/usr/bin/python3
# written by: atholcomb
# dna_generator.py
# dna sequence generator - iteration #2
# Create a DNA sequence from 'atgc' strands

import random
import time

def dna_generator_2():
  num_sequences = 10
  strand = "atgc"
  
  print("[START] Sequence Generation [START]")
  for n in range(1, num_sequences+1):
    print(f"Sequence {str(n).zfill(2)}: ", end='')
    time.sleep(1)
    #print(f"DNA Strand: ", end='')
    for i in range(15):
      print(random.choice(strand), end='')
    print()

dna_generator_2()
