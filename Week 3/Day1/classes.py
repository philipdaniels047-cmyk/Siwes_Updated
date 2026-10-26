#creating a class
class Vehicle:
    def moves(self):
        print('moves along....')
        
#creating an object from the class above.
my_car= Vehicle()

my_car.moves()




class Vehicle:
    def __init__(self, make, model):
        self.make= make
        self.model= model
    
    def moves(self):
        print('moves along....')
        
#creating an object from the class above.
my_car = Vehicle ('Toyota' , 'Corolla')
print(my_car.make)
print(my_car.model)
print (f"I'm a {my_car.make} {my_car.model}")
my_car.moves()



