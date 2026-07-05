#!/usr/bin/python3
# written by: atholcomb
# arithmetic_operation.py
# Create a function to perform basic arithmetic operations that includes 
# addition, subtraction, multiplication and division on a string number.

def arithmetic_operation(string):
  values = string.split()
  operators = []
  numerals = []
  answer = 0
  
  for value in values:
    if "+" in value or "-" in value or "*" in value or "//" in value:
      operators.append(value)
    else:
      numerals.append(value)

  for op in range(0, len(operators)):
    answer = numerals[0], operators[op], numerals[1]

  result = ' '.join(answer)

  if "0" in answer:
    return f"{answer} = -1, division by zero"
  else:
    return f"{answer} = {eval(result)}"


print(arithmetic_operation("12 + 12"))
print(arithmetic_operation("12 - 12"))
print(arithmetic_operation("12 * 12"))
print(arithmetic_operation("12 // 0"))
