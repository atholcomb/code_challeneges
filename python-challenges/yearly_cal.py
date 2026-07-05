#!/usr/bin/python3
# written by: atholcomb
# yearly_cal.py
# Given a list of months, return the number of days in each month

def calendar(months):
  yearly_cal = {}  
  
  for month in months:
    if month == "Feb":
      yearly_cal[month] = 28
    elif month == "Apr" or month == "Jun" or month == "Sep" or month == "Nov":
      yearly_cal[month] = 30
    else:
      yearly_cal[month] = 31

  print("Month\t", "# of days")
  for key, value in yearly_cal.items():
    print(key, "\t", value, "days")

def main():
  calendar(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])

if __name__ == "__main__":
        main()
