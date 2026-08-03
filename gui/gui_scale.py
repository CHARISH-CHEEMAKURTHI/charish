from tkinter import *

def submit():
    print("The temperature is: "+ str(scale.get())+ " degrees C")

window = Tk()

hotImage = PhotoImage(file='../../i_like.png')
hotLabel = Label(image=hotImage)
hotLabel.pack()

scale = Scale(window,
              from_=100,
              to=0,
              length=1000,
              # width=500,
              orient=HORIZONTAL, #orientation of scale
              font = ('Consolas',20),
              tickinterval = 10, #adds numeric indicators for value
              #showvalue = 0, #hide current value
              resolution = 5, #increment of slider
              troughcolor = '#69EAFF',
              fg = '#FF1C00',
              bg = '#111111'

              )
scale.set(((scale['from']-scale['to'])/2)+scale['to']) #set current value of slider

scale.pack()

coldImage = PhotoImage(file='../../i_like.png')
coldLabel = Label(image=coldImage)
coldLabel.pack()

button = Button(window,text='submit',command=submit)
button.pack()

window.mainloop()