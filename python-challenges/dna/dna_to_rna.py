#!/usr/bin/python3
# written by: atholcomb
# dna_to_rna.py
# Transcribe the given DNA strand into corresponding mRNA - a type of RNA, 
# that will be formed from it after transcription. DNA has the bases 
# A, T, G and C, while RNA converts to U, A, C and G respectively.

# header
print("DNA to RNA Transcription Results")
print("--------------------------------")

def dna_to_rna(string):
  strand = ""
  transcription = ""

  # store transcription results
  for s in string:
    if 'A' in s:
      strand = 'U'
    elif 'T' in s:
      strand = 'A'
    elif 'G' in s:
      strand = 'C'
    elif 'C' in s:
      strand = 'G'
    transcription += strand

  # set width of 22 for heading
  print(f"{'DNA:':<{22}}", "RNA:")

  # set width of 22 for values
  print(f"{string:<22} {transcription}")

  # newline for spacing
  print()


dna_to_rna("ATTAGCGCGATATACGCGTAC")
dna_to_rna("CGATATA")
dna_to_rna("GTCATACGACGTA")
