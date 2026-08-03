# button

from tkinter import *

windows=Tk()
like_button=PhotoImage(file="../../i_like.png")
windows.config(background="black")
def click():
    print("you clicked the button")
like=Button(windows,
            text="click hear",
            command=click,
            font=GROOVE,
            fg="green",bg="gold",
            activeforeground="yellow",
            activebackground="red",
            state=ACTIVE,
            # state=DISABLED,
            image=like_button,
            compound="bottom")
like.pack()

windows.mainloop()