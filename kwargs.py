# **kwargs  =   parameter that will pack all arguments into a dictionary
#               usefull so that a function can accept a varying amount of keyword arguments

#def hello(first, last):
#    print("Hello "+first+ " "+ last)

def hello(**names):
   #print("Hello " + kwargs['first'] + " " + kwargs['last'])
    print("Hello",end=" ")
    for key,value in names.items():
        print(value,end=" ")

hello(title="Mr.",first="Le",middle ="Tran Nhat",last="Dang")