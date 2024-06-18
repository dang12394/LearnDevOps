# keyword arguments = arguments preceded by an identifier when we pass them to a function
#                    The order of the arguments doesn't matter, unlike positional arguments
#                   Python knows the names of the arguments that our function receives

def hello(first, middle, last):
    print("Hello " + first + " " + middle + " " + last)

first = "nthing"
hello("Le Tran", "Nhat", "Dang")
hello(last="Dang", first="Le Tran", middle="Nhat")

hello("Letran","n","D")
print(first)