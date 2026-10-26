#lists
users = ['Dave', 'John', 'Sarah']
list = ['Dave', 42, 'true']
emptylist = []

print ('dave' in users)
print (42 in list)  #supposing you want to cofirm a value in a list
print(users[0])     #supposing you want to confirm the position of a particular value
print(list[-1])     #supposing you want to confirm the last value of a list
print(users.index('John')) #supposing you want to know the index of a value, or its position
print(len(users))   #supposing you want to know the length of the list.

list.append('Elsa') #supposing you want to add a value to the list
print(list)
list += ['Jason']   #supposing you want to add a list to another list.
print(list)
list.extend(['Jon Snow', 'Ayra'])
print(list)

list.insert(1, 'Philip')    #supposing you want to insert a value in a position of your choice
print(list)
list.remove('Elsa')
print(list)
list.pop()
print(list)

del users[0]
print(users)            #supposing you want to delete a particular value in a certain position
users.sort()
print(users)            #supposing you want to sort values in alphabetical order.

nums = [4, 42, 5, 4, 1]
nums.reverse()
print(nums)             #supposing you want your values in reverse.
nums.sort(reverse = True)
print(nums)             #supposing you want your values in reverse descending order.
print(type(nums))


#Tuples

