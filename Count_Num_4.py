#!/bin/python
#program to count the number four in a given List
lst=[]
n=int(input("please enter the number of the elements in the List: "))
for i in range (0,n,1) :
    elements=int(input("please enter your list of numbers: "))
    lst.append(elements)
print (lst)
print (lst.count(4))
