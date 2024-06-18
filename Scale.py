from tkinter import *

def submit():
    print("The temperature is: " +str(scale.get())+" degree C")

window = Tk()

hotImage = PhotoImage(file="logo.png")
hotLabel = Label(image=hotImage)
hotLabel.pack()

scale = Scale(window,
              from_=100,
              to=0,
              length=600,
              orient=VERTICAL,
              font =("Consolas",20),
              tickinterval=10, #add numeric indicator for value
              showvalue=0,#hide current value
              resolution=5,#increment of slider
              troughcolor="#69EAFE",
              fg="#FF1C00",
              bg="black"
              )
scale.set(((scale['from']-scale['to'])/2)+scale['to'])  #set current value
scale.pack()

coldImage = PhotoImage(file="logo.png")
coldLabel = Label(image=coldImage)
coldLabel.pack()

button = Button(window,text="submit",command=submit)
button.pack()

window.mainloop()