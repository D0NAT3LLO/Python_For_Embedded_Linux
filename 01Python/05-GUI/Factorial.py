from tkinter import *
import math

master=Tk()
master.title("Factorial")
master.geometry("300x100")
master.resizable(False,False)


def Factorial():
    global entry_N
    fact_label.config(text=f"the Factorial of {entry_N.get()} is: {math.factorial(entry_N.get())}")


Label(master,text="Enter Value of integer N: ").grid(row=1,column=0)
entry_N= IntVar()
e1=Entry(master,textvariable=entry_N)
e1.grid(row=1,column=1)

fact_label=Label(master)
fact_label.grid(row=2,column=1)

Validate_button= Button(master,text="Validate",command=Factorial).grid(row=3,column=1)

master.mainloop()
