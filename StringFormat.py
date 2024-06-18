# str.format()=     optional method that gives users
#                   more control when display output

#animal = "cow"
#item = "moon"

#print("The "+animal+" jumped over the "+item)
#print("The {} jumped over the {}".format(animal,item))
#print("The {1} jumped over the {0}".format(animal,item)) #positional argument
print("The {animal} jumped over the {item}".format(animal="cow",item="moon")) #keyword argument
#text = "The {} jump over the {}"

#print(text.format(animal,item))

name = "Dang"

print("Hello, my name is {}".format(name))
print("Hello, my name is {:10}. Nice to meet you".format(name))
print("Hello, my name is {:<10}. Nice to meet you".format(name))
print("Hello, my name is {:>10}. Nice to meet you".format(name))
print("Hello, my name is {:^10}. Nice to meet you".format(name))

number = 3.14159
number2 = 1000

print ("The number pi is {:.2f}".format(number)) #first 2 number after .
print ("The number pi is {:,}".format(number2)) #add ,
print ("The number pi is {:b}".format(number2)) #binary
print ("The number pi is {:0}".format(number2)) #octave
print ("The number pi is {:X}".format(number2)) #hexa
print ("The number pi is {:,E}".format(number2)) #scienctist






