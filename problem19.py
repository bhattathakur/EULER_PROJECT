'''
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''
from datetime import date

#couting the number of sundays between two dates if sunday is the first day of the month

def sundays(year1, year2):
  num_sundays = 0
  for i in range(year1, year2+1):
      for j in range(1, 13): #12 months
          if date(i, j, 1).weekday() == 6: #date.weekday() returns interger day starting Monday as 0
              #date(year,month,day)
              num_sundays += 1
  return num_sundays

#getting the number of sunday if it is a first day of the month
print(sundays(1901,2000))
