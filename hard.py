from tkinter import *
from tkinter import ttk
import random




def rdpassword(event):
     chars = 'asdokqweokasdflkslkfdsdk544825@'
    
     number_b = int(number_a.get())
     password = ' '
     

     for i in range(number_b):
         password += random.choice(chars)
    #print(password)
         result.set(password)
        







GUI = Tk()
GUI.title('Hard to hack')
GUI.geometry('500x500')





#------------------ROW1---------------------

number_a = StringVar()
result = StringVar()


L1= ttk.Label(GUI, text='How length of password?: ')
L1.grid(row=0,column=0,padx=10,pady=10)

E1 =ttk.Entry(GUI,textvariable= number_a)
E1.grid(row=0,column=1)
E1.bind('<Return>',rdpassword)


L2= ttk.Label(GUI, text='result')
L2.grid(row=1,column=0)

L3= ttk.Entry(GUI,textvariable = result )
L3.grid(row=1,column=1,padx=10,pady=10)











GUI.mainloop()

#rdpassword()
