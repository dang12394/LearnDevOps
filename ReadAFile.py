try:
    with open('ReadAFile.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found:(")