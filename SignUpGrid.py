#Sign Up page using grid geometry

from tkinter import *
from tkinter import ttk

root = Tk()

frame = ttk.LabelFrame(root)
frame.grid(row = 0, column = 0)
frame.grid_propagate(False)
frame.config(height = 200, width = 400)
frame.config(text = "Sign Up")



textboxName = ttk.Entry(frame,text ='Name')
textboxName.grid(row=0,column=0)

textboxEmail = ttk.Entry(frame,text ='Email')
textboxEmail.grid(row=1,column=0)

textboxPassword = ttk.Entry(frame,text ='Password')
textboxPassword.grid(row=2,column=0)

root.mainloop()