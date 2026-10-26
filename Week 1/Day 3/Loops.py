# #while loop
# value = 60
# while value < 100:
#     print(value)
#     value +=5 #basic while loop
# print(" ")

# #while loop with break
# value = 60
# while value < 100:
#     print(value)
#     if value==75:
#         break
#     value +=5           #basic while wiith break statment loop
# print(" ")

# #while loop with continue.
# value = 60
# while value < 100:
#     value +=5
#     if value==75:
#         continue
#     print(value)        #basic while wiith continue statment loop
    






#for loops
names = ["Ugo", "Daniel" , "Uzo"]
for x in names:
    print(x)
    
for x in "hygromentalization":
    print(x)

for x in names:
    if x == "Daniel" :
        break
    print(x)
    
for x in names:
    if x == "Daniel" :
        continue
    print(x)
else: print("Lave ett")
print(' ')

#for loops with range.
for x in range(5):
    print(x)
print (' ')
 
for x in range(60, 101, 5):
    if x== 80:
        break
    print(x)
print(' ')

#nested loops
players = ["Messi", "Ronaldo" , "Neymar"]
statments = ["the goat", "scores goals", "the trickstar"]
for statment in statments:
    for player in players:
        print(player + " " + statment + ".")