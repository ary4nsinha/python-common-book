# write a python program to check whether the given year is leap or not.

import calendar

def checkLeapYear(year):
        print(calendar.isleap(year))
        #add try except block in future to check if input is valid 

year = int(input("Enter the year: "))
checkLeapYear(year)