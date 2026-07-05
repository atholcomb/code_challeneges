#!/usr/bin/python3
# written by: atholcomb
# get_student_names.py
# Create a function that takes a dictionary of student names and returns a list of student names in alphabetical order.

def get_student_names(dict1):
    result = []

    for key, value in dict1.items():
        result.append(value)

    return sorted(result)

print(get_student_names({
  "Student 1" : "Steve",
  "Student 2" : "Becky",
  "Student 3" : "John"
}))
# Should output ["Becky", "John", "Steve"]
