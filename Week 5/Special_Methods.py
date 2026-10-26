class Cars:
    
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
        
    def __repr__(self):
        pass
    def __str__(self):
        pass
        

car_1= Cars('Toyota', 'Camry', 60000,)
car_2= Cars('Bugati' , 'Shevron', 900000,)

print(car_1.company)
print(car_1.amount)
car_1.raise_amount()
print(car_1.amount)
print(car_2.company)


