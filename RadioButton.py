from tkinter import *

food = ["pizza","hamburger","hotdog"]

def order():
    if (x.get()==0):
        print("You order pizza!")
    elif(x.get()==1):
        print("You order a hamburger!")
    elif(x.get()==2):
        print("You order a hotdog!")
    else:
        print("Huh?")

window = Tk()

pizzaImage = PhotoImage(file = 'logo.png')
hamburgerImage = PhotoImage(file = 'logo.png')
hotdogImage = PhotoImage(file = 'logo.png')

foodImages=[pizzaImage,hamburgerImage,hotdogImage]

x = IntVar()

for index in range(len(food)):

    radiobutton = Radiobutton(window,
                              text=food[index], #add text to radio buttons
                              variable=x, #groups radiobuttons together if they share the same variable
                              value=index,#assigns each radiobutton a different value
                              padx=25,#adds padding on x-axis
                              font=("Impact",50),
                              image=foodImages[index], #add image to radio button
                              compound='left',#add image & text
                              indicatoron=0, #eliminate circle indicators
                              width =375, #sets width of radio button
                              command=order #set command of radio button to function
                              )
    radiobutton.pack(anchor=W)


window.mainloop()