from tkinter import *

def doSomething(event):
    print("Mouse cordinates: "+ str(event.x)+"," +str(event.y))

window = Tk()

window.bind("<Button-1>",doSomething) #Left Mouse
window.bind("<Button-2>",doSomething) #Middle Mouse
window.bind("<Button-3>",doSomething) #RightMouse
window.bind("<ButtonRelease>",doSomething) #Release
window.bind("<Enter>",doSomething) #Enter the Window
window.bind("<Motion>",doSomething) #Where the mouse moved


window.mainloop()