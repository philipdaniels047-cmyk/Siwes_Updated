#logical operators and(when both operands are true)
print( True and True)
print(False and False)
print(True and False)

#and used on expressions
expr = (5==5) and (4==6)
print(expr)

x= 4
expr2 = (x>3) and (8<x)
print(expr2) #false because the right operand is false,

#or operator gives a return 'True' if either of the operands is true
print( True or True)
print(False or False)
print(True or False)

#or operators with expressions
y= 6
expr3 = (y>3) or (10<y)
print (expr3)

#Not operator, returns True if the operand is false and vice versa
print(not(True))        #false
print(not(False))       #true

#not with expresion
expr4 = (not(10>20))
print(expr4)