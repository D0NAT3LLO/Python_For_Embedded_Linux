#!/bin/python
#This code is made to represent the ASCII Value of a given Character

from readchar import readkey
import sys
print("Please Enter a Character")
Character=readkey()
sys.stdout.write("ASCII Value is: ")
sys.stdout.write(str(ord(Character)))
