#!/usr/bin/python3
# written by: atholcomb
# get_loglines.py
# For a given log file, return the message body of 
# the log file with the date associated with it

def get_loglines(logfile):
  lines = {}    # declare a dictionary

  for logline in logfile:
    if '9/8/2021' in logline[0]:      # search for a specific date at the 0th index
      lines[logline[5]] = logline[0]  # add the message and date into the dict; make message the key so it's unique each time

  return lines 

# date, followed by arbitary values, then message body
print(get_loglines([['9/7/2021', 54, 56, 57, 58, 'hello world'],['9/8/2021', 54, 56, 57, 58, 'netstat'],['9/8/2021', 54, 56, 57, 58, 'root'],['9/10/2021', 54, 56, 57, 58, 'syslogd']]))
