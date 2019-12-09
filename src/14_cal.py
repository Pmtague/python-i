"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

# Create a calendar

# c = calendar.TextCalendar(calendar.SUNDAY)
# str = c.formatmonth(2019, 11)
# print(str)

# Set the default to the current month using datetime module

user_input = input("Please enter 1-12 for the month and 4 digit year (ex: 11, 1978): ").replace(" ", "").split(",")

def cal(*args):
  new_cal = calendar.TextCalendar(calendar.SUNDAY)
  month = datetime.today().month
  year = datetime.today().year
  day = datetime.today().day

  if len(args) == 1:
    try:
      month_int = int(args[0])
      date = datetime(year, month_int, day)
      print(new_cal.prmonth(date.year, date.month))
    except:
      print(new_cal.prmonth(year, month))

  elif len(args) == 2:
    dates = datetime(int(args[1]), int(args[0]), day)
    print(new_cal.prmonth(dates.year, dates.month))
  
  else:
    print("Please enter a month, or month and year in the following format: XX, XXXX")

cal(*user_input)

# Set boundaries for arguments