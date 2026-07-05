#!/usr/bin/python3
# written by: atholcomb
# countdown.py
# Create a function where given the number n to count down from, and some words string, 
# return a countdown sequence as a string leading up to the words at the end.
# Put a full stop after each number and uppercase and add an exclamation mark to the word.

def countdown(n, string):
  result = []
    
  for num in range(n, 0, -1):
    result.append(str(num))

  return f"{'. '.join(result)}. {string.upper()}!"

print(countdown(10, "Blast Off")) # 10. 9. 8. 7. 6. 5. 4. 3. 2. 1. BLAST OFF!
print(countdown(3, "go")) # 3. 2. 1. GO!
print(countdown(5, "FIRE")) # 5. 4. 3. 2. 1. FIRE!
