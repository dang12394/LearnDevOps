from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\dang1\\OneDrive\\PycharmProjects\\PythonProject",
                                          title="Open file okay?",
                                          filetypes=(('text files',"*.txt"),
                                          ("all files","*.*")))
    #print(filepath) #print file path
    file= open(filepath,"r")
    print(file.read())
    file.close()

window = Tk()

button = Button(window,text="Open",command=openFile)
button.pack()


window.mainloop()