from tkinter import*
from  tkinter.ttk import *
from  tkinter import  Tk ,font
from time import strftime
import datetime
# For Clock
root = Tk()
root.title("clock")
def time():
    string=strftime('%I:%S:%M pm' )
    label.config(text = string)
    label.after(1000,time)
#for Digital clock
label = Label(root,font=('ds-digital',60),background = "black", foreground ="cyan")
label.pack(anchor='center')
time()
mainloop()