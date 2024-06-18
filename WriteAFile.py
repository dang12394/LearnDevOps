text = "Yooooooooo\nThis is some text\nHave a good one!\n"
text2 = "Added text"

with open('WriteAFile.txt','w') as file:
    file.write(text)
with open("WriteAFile.txt",'a') as file: #add to the text
    file.write(text2)