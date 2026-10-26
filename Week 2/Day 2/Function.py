def hello():
    print("Hello World!")
    
hello()         #simle funtion
print(' ')

def hello_world():
    print("Hiii!")
    
hello_world()  #sunctions with more than one word.
print(' ')

def sum(num1, num2):
    print(num1 + num2)
    
sum(2, 3)
sum(8, 15)
sum(6, 6)       #functions using placeholder/parameters
print(' ')

def sum(num1, num2):
    return (num1 + num2)

Total= sum(9, 2)
print(Total)  #value stored in a variable
print(' ')

def sum(num1, num2):
    if type(num1) is not int or type(num2) is not int:
        return "unexpected errror. Plese type in an interger"
    return num1 + num2

total = sum ("a", 3)
print(total) #no specified value after the return
print(' ')

def multiple_items(*args):
    print(args)         
    print (type(args)) #positinal arguments of an unknown number.

multiple_items("Philip", "Ayo", "Joy")
print(' ')

def multi_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))  #receive an arbitrary number of named arguments
    
multi_named_items(first="Philip" , Last="Otobo")




