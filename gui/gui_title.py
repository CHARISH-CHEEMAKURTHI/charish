# tittle

from tkinter import *

windows=Tk()

windows.geometry("1000x500")
windows.title("my first gui")
icon=PhotoImage(file="../../i_eagle man title.png")
windows.iconphoto(True,icon)

windows.mainloop()