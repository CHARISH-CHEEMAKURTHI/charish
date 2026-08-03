# entrybox

from tkinter import *

windows=Tk()

def click():
    a=entry.get()
    print("you entered :" + a)
    entry.config(state=DISABLED)
    # count+=1
    # print(count)
    # exit()
def click1():
    entry.delete(len(entry.get())-1,END)
def click2():
    entry.delete(0,END)

count=0

entry=Entry(windows,font=15,show="*")
submit=Button(windows,text="submit",font=(15),fg="orange",bg="black",activeforeground="white",command=click)
backspace=Button(windows,text="backspace",font=(15),fg="orange",bg="black",activeforeground="white",command=click1,)
delete=Button(windows,text="delete",font=(15),fg="orange",bg="black",activeforeground="white",command=click2,)

entry.insert(0,"enter something")
windows.geometry("500x500")

entry.pack()
submit.pack(side="bottom")
backspace.pack(side="bottom")
delete.pack(side="bottom")

windows.mainloop()