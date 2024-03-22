#Login page using place geometry

from tkinter import *
from tkinter import ttk

root = Tk()

root.title('Login Page')
root.geometry("350x250+10+10")

username_label = ttk.Label(root, text='Username:')
username_label.place(x=75,y=75)

textboxUsername = ttk.Entry(root)
textboxUsername.place(x=140,y=75)

password_label = ttk.Label(root, text='Password:')
password_label.place(x=75,y=100)

textboxPassword = ttk.Entry(root)
textboxPassword.place(x=140,y=100)

login_button = ttk.Button(root,text='Login')
login_button.place(x=160,y=140)

root.mainloop()