# checkbox

from tkinter import *

windows=Tk()

def yes():
    if x.get()==1:
        print("agreed")
    else:print("did`t agreed")


x=IntVar()

check=Checkbutton(windows,text="agree and continue",
                  variable=x,
                  onvalue=1,
                  offvalue=0,
                  command=yes)

check.pack()

windows.mainloop()