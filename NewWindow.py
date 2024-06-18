from tkinter import *

def create_window():
    new_window = Toplevel() #New window 'on top' of other windows, linked to a 'bottom' window
    window.destroy()        #close out of old window, use with Tk

window = Tk()

Button(window,text="Create new window",command=create_window).pack()

window.mainloop()