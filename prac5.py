from tkinter import *
from tkinter import messagebox
master = Tk()
master.geometry('500x200')
def func():
    messagebox.showinfo( "Hello Educba", "Press any key on the keyboard")

b1 = Button( master, text='Click me for next step', background = 'Cyan', fg = '#000000', command = func)
b1.pack()
def Keyboardpress( key):
    key_char = key.char
    print( key_char, 'key button is pressed on the keyboard')
master.bind( '<Key>', lambda i : Keyboardpress(i))
master.mainloop()
