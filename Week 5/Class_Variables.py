#creating a class with attributes and methods, using the __init__ method to initialize the attributes of the class.
class Employee:
    
    num_of_emps = 0  #class variable that keeps track of the number of employees created.
    raise_amount = 1.04  #class variable that is shared among all instances of the class.
    def __init__(self, first, last, pay):   #__init__ method is a constructor that initializes the attributes of the class.
        
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay
        
        Employee.num_of_emps += 1  #incrementing the class variable num_of_emps by 1 each time a new instance of the class is created.
   
    def fullname(self):                                                #fullname method returns the full name of the employee.
        return '{} {}'.format(self.first, self.last)                #returns the full name of the employee by formatting the first and last name attributes.
    def apply_raise(self):
        self.pay = int(self.pay * 1.04)
        
print(Employee.num_of_emps)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

emp_1.apply_raise()
emp_2.apply_raise()
print(emp_1.pay)
print(emp_2.pay)
print(emp_1.__dict__)  #prints the attributes of the emp_1 instance in a dictionary format.
print(emp_1.apply_raise())  #calls the apply_raise method of the emp_1 instance and prints the updated pay attribute.
print(Employee.num_of_emps)  #prints the total number of employees created by accessing the class variable num_of_emps.