
import os
import tkinter as tk

topWin=tk.Tk()
topWin.title("Simple FaceID")

def StartCamera():
    os.system('python camera.py')
    
def ReTraining():
    os.system('python training.py')

def RegisterNew():
    content = E1.get()
    RegExe = 'python Taking_pic.py '+ content
    os.system(RegExe)    

Btn1 = tk.Button(topWin,text="start camera",command= StartCamera,height = 3, width = 15)
Btn1.grid(row=1, column=1)
#Btn1.pack()

Btn2 = tk.Button(topWin,text="Training Again",command= ReTraining,height = 3, width = 15)
Btn2.grid(row=2, column=1)
#Btn2.pack()

L1 = tk.Label(topWin, text = "User Name")
L1.grid(row=3, column=1)

E1 = tk.Entry(topWin, bd = 3)
E1.grid(row=3, column=2)


Btn3 = tk.Button(topWin,text="Register New",command= RegisterNew,height = 3, width = 15)
Btn3.grid(row=4, column=1)
#Btn3.pack()

topWin.mainloop()