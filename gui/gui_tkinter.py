# tittle

from tkinter import *

windows=Tk()

windows.geometry("1000x500")
windows.title("my first gui")
icon=PhotoImage(file="../../i_eagle man.png")
windows.iconphoto(True,icon)

windows.mainloop()

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