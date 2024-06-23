#!/bin/python
#Print the calendar for a given month 
#pip install calendar
import calendar
Year=int(input("please enter the Year: "))
Month=int(input("please enter the Month: "))
print(calendar.month(Year,Month))