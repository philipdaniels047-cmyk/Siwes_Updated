class Cars:
    
    num_of_cars=0
    raise_amt = 1.05        #class variable
    
    def __init__(self, make, model, amount):
        self.make=make 
        self.model=model 
        self.amount=amount
        self.company= make + '.' + model
        
         
    def carname(self):
        return'{} {}' .format(self.make, self.model)
    def raise_amount(self):
        self.amount=int(self.amount * 1.05)
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount
    
car_1= Cars('Toyota', 'Camry', 60000)
car_2= Cars('Bugati' , 'Shevron', 900000)

Cars.set_raise_amt(1.07)


print(Cars.raise_amt)
print(car_1.raise_amt)
print(car_2.raise_amt)



# print(car_1.model)
# print(car_1.make)
# car_1.raise_price()
# print(car_1.price)
# print(car_1.company)
# print(Cars.carname(car_2))
# car_2.raise_price()
# print(car_2.price)
