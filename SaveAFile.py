from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\dang1\\OneDrive\\PycharmProjects\\PythonProject",
                                    defaultextension='.txt',
                                    filetypes=[
                                        ("Text Document",".txt"),
                                        ("HTLM Document",".html"),
                                        ("All files",'.*')
                                    ])
    if file is None:
        return 
    filetext = str(text.get(1.0,END))
    #filetext = input("Enter some txt :") #use console to enter value
    file.write(filetext)
    file.close()
window = Tk()

button = Button(window,text="Save",command=saveFile)
button.pack()
text = Text(window)
text.pack()

window.mainloop()