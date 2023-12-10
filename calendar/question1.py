#import calendar
#print(calendar.month(2020,1))
#trash code 

#write a python program to display a particular month of a year using calendar module.

import calendar

def display_month(year, month):
    try:
        cal = calendar.month(year, month)
        print(f"Calendar for {calendar.month_name[month]} {year}:\n")
        print(cal)
    except IndexError:
        print("Invalid month. Month should be in the range 1 to 12.")

year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))

display_month(year, month)
