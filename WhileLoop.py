#while lopp = a statement that will execute its block of code,
#               as long as its condition remains true

#while 1==1:
#   print("Help! I'm stuck in a loop!")

name = None

#while len(name) == 0:
while not name:
    name=input("Enter your name: ")

print("Hello "+ name)