# name = "Alice"
# age = 30

# # Simple variable substitution
# message = f"Hello, {name}! You are {age} years old."
# print(message)

# #old methods of formatting strings.
# person = "dave"
# coins = 50
# print("\n" + person + "has" + str(coins) + "coins left.")

# # %s method
# message= "\n%s has %s coins left." %(person, coins)
# print(message)

# #.format method
# message = "\n {} has {} coins left.".format (person, coins)
# print(message)

# #format method but using index numbers.
# message = "\n {1} has {0} coins left.".format (coins, person)
# print(message)

# #format method setting the values of the parameters.
# message = "\n {person} has {coins} coins left.".format (person=person , coins=coins)
# print(message)

# player={'person': 'dave', 'coins': 3}

# #format method using dictionaries.
# message = "\n {person} has {coins} coins left.".format (**player)
# print(message)



#f-strings! the way!
person = "Philip"
coins = 6
message = f"\n {person} has {coins} coins left"
print(message)

#f strings with math operation
message = f"\n {person} has {2*5} coins left"
print(message)

#f strings with methods
message = f"\n {person.lower()} has {2*9} coins left"
print(message)

player ={'person': 'Philip','coins':3}

#f strings working with dictionaries.
message = f"\n {player['person']} has {player['coins']} coins left"
print(message)

########
#Passing formatting options in f strings
num = 10
print(f"\n2.25 times {num} is {2.25 * num:.2f}")

for num in range(1 ,11):
    print(f"\n2.25 times {num} is {2.25 * num:.2f}")