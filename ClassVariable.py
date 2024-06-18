from Carlist import Car

car_1 = Car("Chevy","Covette",2021,"blue")
car_2 = Car("Ford","Mustang",2022,"red")

car_1.wheels = 2
#Car.wheels = 2 #This will effect all the class

print(car_1.wheels)
print(car_2.wheels)

print(Car.wheels)