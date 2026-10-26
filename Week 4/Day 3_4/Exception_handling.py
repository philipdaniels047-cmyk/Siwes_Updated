# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.

try:
    print(x)
except:
    print('There is an error')
   
y= 10 
try:
    print(y)
except NameError:
    print('NameError means undefined variable') #catching a specific error
else:
    print('No errors')


number = int(input("Enter a number: "))
try:
    result = 10 / number
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")
else:
    print('No errors')
finally:
    print('all good')

