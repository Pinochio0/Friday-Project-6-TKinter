#Calculator code for tkinter using pack geometry

from tkinter import *
from tkinter import ttk

root = Tk()

#defines window size
root.geometry("500x500+10+10")

textbox = Entry(root)
textbox.pack(side = TOP)



root.mainloop()