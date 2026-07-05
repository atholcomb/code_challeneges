#!/usr/bin/python3
# written by: atholcomb
# cigar_party.py

def cigar_party(cigars, is_weekend):
  if cigars <= 40 and cigars <= 60 and is_weekend == False:
    return False
  elif cigars >= 40 and cigars <= 60 and is_weekend == False:
    return True
  elif cigars > 40 and cigars > 60 and is_weekend == True:
    return True
  elif cigars < 40 and cigars < 60 and is_weekend == True:
    return False
  elif cigars > 40 and cigars < 60 and is_weekend == True:
    return True
  elif cigars > 60 and is_weekend == False:
    return False

print(cigar_party(30, False))
print(cigar_party(50, False))
print(cigar_party(70, True))
print(cigar_party(30, True))
print(cigar_party(50, True))
print(cigar_party(61, False))
