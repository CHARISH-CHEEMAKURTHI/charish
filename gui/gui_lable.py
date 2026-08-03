# label

from tkinter import *

windows=Tk()
images=PhotoImage(file="../../i_eagle man title.png")
title=Label(windows,
            text="welcome",
            font=("arial",40,"italic"),
            fg="gold",
            bg="indigo",
            relief=RAISED,
            bd=10,
            padx=20,
            pady=20,
            image=images,
            compound="top")
title.pack()
# title.place(x=400,y=0)

windows.mainloop()