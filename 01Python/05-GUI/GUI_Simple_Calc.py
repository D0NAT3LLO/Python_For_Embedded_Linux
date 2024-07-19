from tkinter import *

master=Tk()
master.title("Simple_Calc")
master.geometry("500x100")
master.resizable(False,False)

def Calculate():
    global v, N_entry,M_entry #their get() will get integer value without casting
    Decision=v.get()
    # N=e1.get()
    # integer_N = int (N) #typecasting
    # M=e2.get()
    # integer_M = int (M) #typecasting 
    if Decision==1:
        #SUM= integer_N + integer_M
        SUM = N_entry.get() + M_entry.get()
        Sum_label.config(text=f"Sum of {N_entry.get()} & {M_entry.get()} is: {SUM} ")
    elif Decision==2:
        #SUB= integer_N - integer_M 
        SUB = N_entry.get() - M_entry.get()  
        Sum_label.config(text=f"Subtraction of {M_entry.get()} from {N_entry.get()} is: {SUB} ") 

#instead of typecasting !!
N_entry=IntVar(master)
M_entry=IntVar(master)


Label(master,text="Enter the Value of N").grid(row=1,column=0)
Label(master,text="Enter the Value of M").grid(row=2,column=0)
e1_N=Entry(master,textvariable=N_entry)
e1_N.grid(row=1,column=1)
e2_M=Entry(master,textvariable=M_entry)
e2_M.grid(row=2,column=1)
v=IntVar()
Radiobutton(master, text='SUM',variable=v, value=1).grid(row=3,column=0)
Radiobutton(master, text='SUB',variable=v, value=2).grid(row=4,column=0)

Sum_label=Label(master)
Sum_label.grid(row=3,column=2)

Calc_button=Button(master,text="Calculate",command=Calculate).grid(row=4,column=2)
master.mainloop()