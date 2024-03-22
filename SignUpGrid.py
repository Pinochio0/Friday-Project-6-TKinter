#Sign Up page using grid geometry

from tkinter import *
from tkinter import ttk

root = Tk()

root.title('Sign Up')
root.geometry("350x100+10+10")


name_label = ttk.Label(root, text="Name:")
name_label.grid(column=0, row=0)

textboxName = ttk.Entry(root)
textboxName.grid(row=0,column=1)

email_label = ttk.Label(root, text="Email:")
email_label.grid(column=0, row=1)

textboxEmail = ttk.Entry(root)
textboxEmail.grid(row=1,column=1)

password_label = ttk.Label(root, text="Password:")
password_label.grid(column=0, row=2)

textboxPassword = ttk.Entry(root,text ='Password')
textboxPassword.grid(row=2,column=1)

root.mainloop()