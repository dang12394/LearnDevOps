# multi-level inheritance = when a derived (child) class inherits another derived (child) class

class Organism:                                 #Grandparent

    alive = True

class Animal(Organism):                         #Parent

    def eat(self):
        print("This animal is eating")

class Dog(Animal):                              #Child

    def bark(self):
        print("This dog is barking")

dog = Dog()
print(dog.alive)
dog.eat()
dog.bark()