#Calculator code for tkinter using pack geometry

from tkinter import *
from tkinter import ttk

root = Tk()

root.title('Calculator')
root.geometry("350x250+10+10")

textbox = ttk.Entry(root, state=DISABLED)
textbox.pack(side = TOP)

button1 = ttk.Button(root,text = '1',width=4)
button1.pack(side = LEFT)

button2 = ttk.Button(root,text = '2',width=4)
button2.pack(side = LEFT)

button3 = ttk.Button(root,text = '3',width=4)
button3.pack(side = LEFT)

button4 = ttk.Button(root,text = '4',width=4)
button4.pack(side = LEFT)

button5 = ttk.Button(root,text = '5',width=4)
button5.pack(side = LEFT)

button6 = ttk.Button(root,text = '6',width=4)
button6.pack(side = LEFT)

button7 = ttk.Button(root,text = '7',width=4)
button7.pack(side = LEFT)

button8 = ttk.Button(root,text = '8',width=4)
button8.pack(side = LEFT)

button9 = ttk.Button(root,text = '9',width=4)
button9.pack(side = LEFT)

#---------------------------------------

buttonplus = ttk.Button(root,text = '+',width=4)
buttonplus.pack(side = BOTTOM)

buttonminus = ttk.Button(root,text = '-',width=4)
buttonminus.pack(side = BOTTOM)

buttonmultiply = ttk.Button(root,text = 'x',width=4)
buttonmultiply.pack(side = BOTTOM)

buttondivide = ttk.Button(root,text = '/',width=4)
buttondivide.pack(side = BOTTOM)



root.mainloop()