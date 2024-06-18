from tkinter import *

#widgets = GUI elements: buttons, textboxes, labels, images
#windows = servers as a container to hold or contain  these widgets

window = Tk() #instantiate an instance of a window
window.geometry("420x420")
window.title("Nhat Dang first GUI program")

icon = PhotoImage(file = 'logo.png')
window.iconphoto(True,icon)
window.config(background="#2ffaec")
window.mainloop() #place window on computer screen, listen for events