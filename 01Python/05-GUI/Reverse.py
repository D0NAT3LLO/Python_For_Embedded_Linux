from tkinter import *
master=Tk()
master.title("Reverse")
master.geometry("300x100")
master.resizable(False,False)

def Reverse():
    variable=entry.get()
    txt=variable[::-1]
    Reverse_label.config(text=f"Reverse is : {txt}")

Label(master,text='Enter the String:').grid(row=0,column=0)
entry=Entry(master)
entry.grid(row=0,column=1)

Reverse_label=Label(master)
Reverse_label.grid(row=1,column=1)

Reverse_Button=Button(master,text="Reverse",command=Reverse).grid(row=2,column=1)
master.mainloop()