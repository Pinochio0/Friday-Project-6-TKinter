#Calculator code for tkinter using pack geometry

from tkinter import *
from tkinter import ttk

root = Tk()

textbox = ttk.Entry(root, state=DISABLED)
textbox.pack(side = TOP)

button1 = ttk.Button(root,text = '1')
button1.pack(side = LEFT)

button2 = ttk.Button(root,text = '2')
button2.pack(side = LEFT)

button3 = ttk.Button(root,text = '3')
button3.pack(side = LEFT)

button4 = ttk.Button(root,text = '4')
button4.pack(side = LEFT)

button5 = ttk.Button(root,text = '5')
button5.pack(side = LEFT)

button6 = ttk.Button(root,text = '6')
button6.pack(side = LEFT)

button7 = ttk.Button(root,text = '7')
button7.pack(side = LEFT)

button8 = ttk.Button(root,text = '8')
button8.pack(side = LEFT)

button9 = ttk.Button(root,text = '9')
button9.pack(side = LEFT)



root.mainloop()