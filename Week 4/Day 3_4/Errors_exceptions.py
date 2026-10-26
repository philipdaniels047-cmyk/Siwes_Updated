#errors are issues that distrupts the execution of code.

#syntax errors occur when it violates python rules
if True:
    print("Hello")      #SyntaxError: expected ':'

# #runtime errors occur while the program runs with a valid syntax but python cannot execure
x = 10/0
print(x)    #ZeroDivisionError: division by zero 
print (y)    #undefined variable

#logical errors trickiest errors because no error message is produced, and produces incorrect results
num1= 10
num2=20
average = num1 + num2 / 2 #incorrect operator precedence
print(average)




