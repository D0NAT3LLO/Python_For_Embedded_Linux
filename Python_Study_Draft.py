#!/usr/bin/python3


# print("hello")
# x=3.5
# print(x)
# print(type(x))
# print(id(x))

# x=["mostafa" , "Youssef", 1,2,3,4,5,6,7,8,9]
# print(x[0:10:2])
# print(x[4:])
# print(x[-2])
# x[4]=5
# print(x)

# input_name = input("enter ur name ")
# print ("hello " + input_name + "!" )
# age= int(input("enter ur age"))
# print ("you are " + str(age+12) )


# a=[10]
# b=[10]
# print(id(a))
# print(id(b))
# print (a)
# #a.append(20)
# print (a)
# if a is b :
#     print (" a and b have the same identity")
# if a == b :
#     print ("a equals to b")

# i=0
# while i < 10: 
#     print(i,end=" ")
#     i+=1
# for i in range(10):
#     for j in range(10):
#         print(i,end=" ")


# [print(i) for i in "Mostafa"] #short hand for 
# [print(i) for i in range (10) if i%2==0]
#Reversing String
# name=input("please enter your name: ")
# for i in range(len(name)):
#     print(name[-1-i],end="")
# print ()
# txt=name[::-1]
# print (txt)

# import datetime
# print(datetime.datetime.now())
# import pyfiglet
# result=pyfiglet.figlet_format("DONATELO")

# print(result)
# #print ("searching for errorss")

# x="mostafa youssef abdelazim"
# print (x.capitalize())

# age = 30
# name="Mostafa"
# print(f"name {name} age {age} ")
# #List to string
# names=["Mostaf","Youssef","Abdelazim"]
# name=" ".join(names)
# print (name)

# var=r"hi \n Hello"  #r will prevent the effect of  \n
# print (var)
# #center
# print("hello".center(20,"*"))
# #find
# print ("Hello".find("l"))
# #index
# print("halllo".index("l"))

# def my_function():
#     print ("hello from fn")

# my_function()
# def my_function(name): #its ok as its using interpreter
#     print(f"Hello from name {name}")
# x=input ("enter your name:  ")
# my_function(x)

# def func(child1,child2,child3):
#     print("child 1 is: " + child1)
#     print("child 2 is: " + child2)
#     print("child 3 is: " + child3)

# func(child3="Omar",child1="zima",child2="mohamed")

#veridic Fn to assign parameter

# def func(*arg): #TUPLE
#     print(type(arg))
#     for i in arg:
#         print(i)
        
#  func('test','Hello')    


# def myFun(*argv):
#     print(type(argv))
#     for arg in argv:
#         print(arg)

# myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')


# #DICT
# def func(**arg):
#     print(arg["name"])
#     print(arg["age"])
#     print(arg["email"])

# dct={"name":"Mostafa", "age":36  , "email":"ammarmostafa90@gmail.com"}
# func(name="mostafa",age=24,email="ammar@") #passing values to the keys 
# func(**dct) #passsing the whole dict

# x=888
# def func():
#     global x
#     x=555
#     print(x)
#     print(id(x))

# func()
# print(x)
# print (id(x))

#LAMBDA EXP (maily for cllbck)
ls=[1,2,3,4,5,6,7,8,9]
# print(list(map(lambda x : x*x*x,ls)))

# ls=[1,2,3,4,"mostafa","youssef"]
# ls.append("Abdelazim")
# print(ls)
# ls2=ls.copy() #.copy() will prevent the change in ls2 to reflected on ls
# ls2.append(6)
# print(ls2)
# print(ls)
# ls.extend([4.5,4.6])
# print(ls)
# ls.insert(3,"my email")
# print (ls)
# ls.pop() #last thing deleted
# print(ls)
# ls.remove("my email")
# print(ls)
# ls.reverse()
# print(ls)

# import pyautogui
# from time import sleep
# sleep(2)
# while True:
#     print(pyautogui.position())
#     sleep(1)

#ASCII representation (Decimals)
#print(ord('a'))

# class animal:
#     #name = ""
#     __member=15
#     def __init__(self) :
#         print("constructor is called")
#         #self.name =name
#     #testing member...
#     def test(self):
#         print(f'{self.__member}')

#     def eat(self):
#         print("eat smth")
#     def __del__(self):
#         print("Destructor is called")

# class dog(animal):
#     def __init__(self):
#         print("const in dogs is called")

#     def sound(self):
#         print("HOW HOW")

#     def __del__(self):
#         print("dest for dog is called")
#         super().__del__()
# # mydog= dog()
# # mydog.eat()
# # mydog.sound()

# obj=animal()
# obj.test()
# #print(obj.__member) #ERROR
# print(obj._animal__member) #prints 15
            
# import threading
# from time import sleep

# def task1():
#     while True:
#         print('Task1')
#         sleep(1)

# def task2():
#     while True:
#         print('Task2')
#         sleep(1)

# t1= threading.Thread(target=task1).start()
# t2 = threading.Thread(target=task2).start()

# while True:
#     print("Main thread")
#     sleep(1)



# def outer_func(x):
#     def inner_func(y):
#         return x+y
#     return inner_func

# closure = outer_func(5)
# result = closure(3)
# print (result)

# x= [1,2,3]
# y=x
# x.append(4)
# print(y)

# x= 10 
# def func():
#     global x 
#     x+=5
# func()
# print(x)

# list1=[3, 4, 5, 20, 5, 25, 1, 3]

# list1.pop(1) # by index
# print(list1)

# student = {
#     "name":"mostafa",
#     "class" : 10,
#     "marks" : 20
# }
# m = student.get('marks')

# print(m)


# #import tkinter as tk
# from tkinter import *
# window=Tk()
# window.title("Cross_Buttons")
# window.geometry("300x100")
# window.resizable(False,False)
# #window.configure(background="black")
# # Label(window,text="place",fg="red",bg="white").place(x=20,y=50)
# # Label(window,text="grid1",fg="red",bg="white").grid(row=2,column=1)
# # Label(window,text="grid2",fg="red",bg="white").grid(row=1,column=2)

# # #cllbck fn 
# def But1():
#     print("Button 1 is pressed")

# def But2():
#     print("Button 2 is pressed")

# def But3():
#     print("Button 3 is pressed")

# def But4():
#     print("Button 4 is pressed")


# # button = tk.Button(window,text='Exit',width=30,command=window.destroy)
# # button2 = tk.Button(window,text='Led ON',width=30,command=fn_Ledon)
# # button.grid(padx=0,pady=1)
# # button2.pack()

# button1 = Button(window,text="Button1",command=But1).grid(row=0,column=1,)
# button2 = Button(window, text="Button2",command=But2).grid(row=1,column=0,)
# button3 = Button(window, text="Button3",command=But3).grid(row=1,column=2,)
# button4 = Button(window, text="Button4",command=But4).grid(row=2,column=1,)

# # button2 = tk.Button(window,text='Button2',width=10,command=print("Button2 is pressed"))
# # button2.grid(padx=(1,1),pady=(0,0))

# # button3 = tk.Button(window,text='Button3',width=10,command=print("Button3 is pressed"))
# # button3.grid(padx=(1,1),pady=(2,2))

# # button4 = tk.Button(window,text='Button4',width=10,command=print("Button4 is pressed"))
# # button4.grid(padx=(2,2),pady=(1,1))


# window.mainloop()


# from tkinter import *

# master=Tk()
# master.title("ListBox")
# master.geometry("400x400")
# master.resizable(False,False)

# def item_selected(event):
#     selected_index= Lb.curselection()
#     print(selected_index)
#     print(Lb.get(selected_index))


# Lb=Listbox(master)
# Lb.insert(1, 'Python')
# Lb.insert(2, 'C++')
# Lb.insert(3, 'C')
# Lb.insert(4, 'Another')
# Lb.pack()
# Lb.bind('<<ListboxSelect>>', item_selected)

# v= IntVar()

# def DisplayValue():
#     global v
#     print(v.get())

# Radiobutton(master,text='option1',variable=v,value=1).pack(anchor=W)
# Radiobutton(master,text='option2',variable=v,value=2).pack(anchor=W)
# button=Button(master, text="GET",command=DisplayValue)
# button.pack()

# master.mainloop()








