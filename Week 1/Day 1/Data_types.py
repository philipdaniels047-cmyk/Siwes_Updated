#Numbers
x=21
y=22.95
print(x), print(y)
print(x+y)

# #strings
fruits="Pawpaw" , "mangos"
print(fruits)
z= 'I was told that "python was easy to learn, Na lie" ' #single quotes for double quote string.
print(z)

# w= "Python is easy, 'Thats what i was told' . "
# print(w)

# #boolean
# bool = True
# print(bool)
# print(10>5) , print(10<5)
# print(5*3>10)

# #list
# mylist = '5' , '19' , '22'


# #strings data type

# #literal assignments
first= "Agt"
last= "47"
# print(type(first))
# print(type(last))
# print(type(first) == float )
# print(isinstance(first, str))

# #construction assignments
# pizza = str ("Pepperoni")
# print(type(pizza))
# print(type(pizza) == str )
# print(isinstance(pizza, str))

#concatenation of strings
fullname = first + last
print(fullname)
fullname += "!"
print(fullname)

#casting
decade= str (1980)
print(type(decade))
print(decade)
statement = "I love cocks from the " + decade + "s."
print(statement)

#statement with multiple line
multiline = ''' Hey, how are you?

                just checking in.
                        
                        you good?
'''
print(multiline)

#escaping characters
sentence = 'I\'m back at work!\t Hey!\n\n Where\'s this at\\ located?'
print(sentence)

#strings method
name = 'philip' 
print(name)
print(name.lower())
print(name.upper())             #upper and lower case strings
print(sentence.title())        #First letter caps for every word.
print(sentence.replace("back", "here")) #replaced 'back' with 'here'

print(len(sentence))            # counts no of characters in the sentence/string
sentence += "                                                                        "
sentence = "                                 " +   sentence
print(len(sentence))

print(len(sentence.strip()))
print(len(sentence.lstrip()))
print(len(sentence.rstrip()))

print(" ")

#building a menu
game= "menu".upper()         #you can also add a string method directly on a variable.
print(game.center(20, "="))
print("coffee".ljust(16, ".") + "£1".rjust(4))
print("Cake".ljust(16, ".") + "£4".rjust(4))
print("tea".ljust(16, ".") + "£3".rjust(4))

print(" ")

#string index values
print(first[0])         #print the first value of a string
print(first[-1])        #print the last value of a string.
print(first[1])         #print the second value of a string.
print(first[0:-1])         
print(first[0:])         #prints the variable using range. ie from the start to end of the string.
print(" ")

#methods with boolean data
Dayoftheweek= "Monday"
print(Dayoftheweek.startswith("M"))
print(Dayoftheweek.endswith("F"))
print(" ")

#importing modules
import math 
print(math.pi)
print(math.sqrt(64))
print(math.ceil(64))
print(math.floor(64))
