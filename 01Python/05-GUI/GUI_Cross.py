from tkinter import *
window=Tk()
window.title("Cross_Buttons")
window.geometry("300x100")
window.resizable(False,False)

def But1():
    print("Button 1 is pressed")

def But2():
    print("Button 2 is pressed")

def But3():
    print("Button 3 is pressed")

def But4():
    print("Button 4 is pressed")

button1 = Button(window,text="Button1",command=But1).grid(row=0,column=1,)
button2 = Button(window, text="Button2",command=But2).grid(row=1,column=0,)
button3 = Button(window, text="Button3",command=But3).grid(row=1,column=2,)
button4 = Button(window, text="Button4",command=But4).grid(row=2,column=1,)

window.mainloop()