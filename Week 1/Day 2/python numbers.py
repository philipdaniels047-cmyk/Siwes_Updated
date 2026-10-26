#python numbers
a = 3.7952
b = 5
c = 7         
d = 9.966
e = 12j
f = 15j         #complex numbers, it could also be floating points or integers.
print(a+b+c)
print (type (a))
print (type (b))
print (type (c))
print (type (d))
print (type (e))
print (type (f))            #type function to show the the type of numbers.
print(round(d, 2))
print(round(a, 3))          #round function using the number and ndigits syntax

h= pow(10, 2)               #same as 10 * 10
j= pow(20, 4)               #same as 20 * 20 * 20 * 20
print(h)
print(j)            #using the pow() function.
print (h+j)
print(type (h))

#getting an absolute value
k = abs (-4)
z = abs (-3.52)
print(k)
print(z)
print(type (k))
print(type (z))

#quotient and remainder
w= 5
q= 9
print(divmod(w, 2))
print(divmod(q, 3))
print(divmod(70, 5))        #using the divmod() syntax to divide variables and values