from tkinter import *

def openFile():
    print("File has been opened!")

def saveFile():
    print("File has been saved!")

def cutFile():
    print("You cut some text!")

def copyFile():
    print("You copy some text!")

def pasteFile():
    print("You paste some text!")

window = Tk()

openImage = PhotoImage(file="file.png")
saveImage = PhotoImage(file="save.png")
exitImage = PhotoImage(file="exit.png")

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar,tearoff=0,font=("MV Boli",15))
menubar.add_cascade(label = "File",menu=fileMenu)
fileMenu.add_command(label="Open",command=openFile,image=openImage,compound="left")
fileMenu.add_command(label="Save",command=saveFile,image=saveImage,compound="left")
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=quit,image=exitImage,compound="left")

editMenu = Menu(menubar,tearoff=0,font=("MV Boli",15))
menubar.add_cascade(label ="Edit",menu=editMenu)
editMenu.add_command(label="Cut",command=cutFile)
editMenu.add_command(label="Copy",command=copyFile)
editMenu.add_command(label="Paste",command=pasteFile)


window.mainloop()