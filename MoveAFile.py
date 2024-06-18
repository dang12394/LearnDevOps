import os

source = "Move.txt"
destination = "C:\\Users\\dang1\\OneDrive\\Desktop\\Move.txt"
source2 = "Move"
destination2 = "C:\\Users\\dang1\\OneDrive\\Desktop\\Move"

try:
    if os.path.exists(destination2):
        print("There is already a file there")
    else:
        os.replace(source2,destination2)
        print(source2+" was moved")
except FileNotFoundError:
    print(source2+" was not found")