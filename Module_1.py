#1.Module can be run as a standalone program
#2.Module can be imported and used by other modules

#Python interpreter sets "special variables", one of which is __name__
#then Python will execute the code found within __main__
# the initial module being run

# import Module_2
# print(__name__)
# print(Module_2.__name__)

def main():
    print("Hello!")

if __name__== "__main__":
    main()

else:
    pass #print("running other module indirectly")