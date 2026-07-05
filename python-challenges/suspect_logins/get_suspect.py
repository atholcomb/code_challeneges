#!/usr/bin/python3
# written by: atholcomb
# get_suspect.py
# Given a log file with suspect login entries,
# identify date, user and suspect login attempt 

import json

def get_suspect():
  print("**** Entries below are SUSPECT: ****\n")
  for line in open('suspect.log', 'r'):
    data = json.loads(line)
    if data['login'] == 'failed':
      print(line)

get_suspect()
