# value = 60
# while value < 100:
#     print(value) 
#     value+= 2
           #basic while loop
    
# value = 60
# while value < 100:
#     print(value)
#     if value==78:
#         break
#     value+= 2       #while loop with break statement
    
# value = 60
# while value < 100:
#     value+= 2
#     if value==78:
#         continue
#     print(value)     #while loop with continue statement. in this, increment comes first, then the print statement, last.

# value = 1
# while value < 10:
#     value+= 1
#     if value== 7:
#         continue
#     print(value)
# else: 
#     print("Value is equal to"+ str(value))  #while-else is optional when the loop finishes without hitting A BREAK.


#'FOR' LOOP
# names = ["Daniel" , "Philip" , "Oghenetega"]
# for x in names:
#     print(x)       #x or any thing can represent each character in a string.
    
# for x in "Mississipi" :
#     print(x)    #prints every character in the string.
    
# for x in names:
#     if x == "Philip":
#         break
#     print(x)        #for loop with break statment
    
# for x in names:
#     if x== "Daniel":
#         continue
#     print(x)        #for loop with continue statment

#range function in for loops
# for x in range(4):
#     print(x)        #prints from 0-3.
# print(" ")
    
# for x in range(2,4):
#     print(x)        #prints from 2-3.
# print(' ')

# for x in range(0,101,10):
#     print(x)        #prints from 0-100 with an increment of 10.
# print(' ')

# for x in range(5,100,5):
#     print(x)        #prints from 5-95 with an increment of 5.
# else:
#     print('false')
#     print(type(x))
# print(' ')

#Nested Loops
# names = ["Daniel" , "Philip" , "Oghenetega"]
# actions = ["sleep" , "game" , "codes"]
# for name in names:
#     for action in actions:
#         print(name + " " + action+ ".")     #placing the first  loop into the other.
        
# names = ["Daniel" , "Philip" , "Oghenetega"]
# actions = ["sleep" , "game" , "codes"]
# for action in actions:
#     for name in names:
#         print(name + " " + action+ ".")     #placing the first  loop into the other.
        
value = 5
while value < 20:
    value +=2
    if  value == 16:
        continue
    print(value)
else:
    print("No Way !")