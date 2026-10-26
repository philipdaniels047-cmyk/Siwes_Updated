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

class Developers(Cars):
    raise_amt=1.10
    
    def __init__(self, make, model, amount, prog_lang):
        super(). __init__(make, model, amount)
        self.prog_lang=prog_lang
        
class Manager(Cars):
    raise_amt=2.10
    
    def __init__(self, make, model, ammount, name):
        super(). __init__(make, model, ammount, name,)
        self.name = name
    
    
car_1= Manager('Toyota', 'Camry', 60000, 'python' 'M.D. Philip')
car_2= Manager('Bugati' , 'Shevron', 900000, 'java' 'M.D . Julia')

print(car_1.company)
print(car_1.prog_lang)
print(car_2.name)
print(car_1.amount)
car_1.raise_amount()
print(car_1.amount)
print(car_2.company)
print(car_1.prog_lang)

