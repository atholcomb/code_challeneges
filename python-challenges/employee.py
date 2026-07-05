#!/usr/bin/python3
# written by: atholcomb
# full_name_email.py
# Create the instance attributes fullname and email in the Employee class. Given a person's first and last names:
# Form the fullname by simply joining the first and last name together, separated by a space.
# Form the email by joining the first and last name together with a . in between, and follow it with @company.com at the end. 
# Make sure the entire email is in lowercase.

class Employee:
    def __init__(self, first, last, email=None):
        self.fullname = first + ' ' + last
        self.email = (first + '.' + last +'@company.com').lower()
        self.firstname = first


emp_1 = Employee("John", "Smith")
emp_2 = Employee("Mary",  "Sue")
emp_3 = Employee("Antony", "Walker")

print(emp_1.fullname)       # "John Smith"
print(emp_2.email)          # "mary.sue@company.com"
print(emp_3.firstname)      # "Antony"
