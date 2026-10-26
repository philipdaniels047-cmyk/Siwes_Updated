#creating a class with no attributes or methods, using the pass statement to create an empty class.

class Employee:
    pass            #a class with no attributes or methods. An empty class.


emp_1 = Employee()          #Creating an instance of the employee class. emp_1 is an instance of the employee class.
emp_2 = Employee()          #Creating an instance of the employee class. emp_2 is an instance of the employee class.

# print(emp_1)
# print(emp_2)

# #Adding attributes to the emp_1 instance of the employee class.
emp_1.first = 'Corey'   
emp_1.last = 'Schafer'
emp_1.email = 'corey.schafer@company.com'
emp_1.pay = 50000

# #Adding attributes to the emp_2 instance of the employee class.
emp_2.first = 'Test'   
emp_2.last = 'User'
emp_2.email = 'TestUser@company.com'
emp_2.pay = 60000

print(emp_1.email)
print(emp_2.email)
print(emp_2.first, emp_2.last)
print(emp_1.first, emp_1.last)



#creating a class with attributes and methods, using the __init__ method to initialize the attributes of the class.
# class Employee:
#     def __init__(self, first, last, pay): #__init__ method is a constructor that initializes the attributes of the class.
#         self.first = first
#         self.last = last
#         self.email = first + '.' + last + '@company.com'
#         self.pay = pay
#     def fullname(self): #fullname method returns the full name of the employee.
#         return '{} {}'.format(self.first, self.last)                #returns the full name of the employee by formatting the first and last name attributes.

# emp_1 = Employee('Corey', 'Schafer', 50000)
# emp_2 = Employee('Test', 'User', 60000)

# emp_1.fullname() #calling the fullname method of the emp_1 instance of the employee class.
# print(Employee.fullname(emp_1)) #calling the fullname method of the emp_1 instance of the employee class.