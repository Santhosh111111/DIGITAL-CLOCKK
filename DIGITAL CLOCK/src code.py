from tkinter import Tk
from tkinter import Label
import time
import sys


root = Tk()
root.title("LIVE DIGITAL CLOCK")

digi_clock = Label(root,font=("arial" , 150), bg= "black" , fg = "yellow")
digi_clock.pack()

def present_time():
    display_time = time.strftime("%H:%M:%S ")
    digi_clock.config(text=display_time)
    digi_clock.after(200,present_time)


present_time()
root.mainloop()
