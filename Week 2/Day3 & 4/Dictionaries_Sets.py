#Dictionaries
band= {
        "vocal":"plant",
        "guitar":"page"    
}
#with constructor function
band2=dict(vocals= "plant", guitar= "page")
print(band)
print(band2)
print(len(band2))
print(type(band2))


#access items in the dictionary
print(band["vocal"])
print(band.get("guitar"))

#list keys/values in dict
print(band.keys())
print(band.values())

#list of key/value pairs as tuples
print(band.items())

#verify that a key exsist
print("guitar" in band2)
print("Naruto" in band2)
print(type(band.keys))

print(' ')
print(' ')
print(' ')
print(' ')
print(' ')




#changing values in dictionary python
band["vocal"] = "coverdale"
band.update({"base": "JPJ"})
print(band)

#removing values in dict
print(band.pop("base"))
print(band)

band["drums"]= "bonham"
print(band)

print(band.popitem())           #returns a tuple
print(band)

#delete/clear items in dict
band["drums"] = "bonham"
del band ["drums"]
print(band)

band2.clear()
print(band2)

del band2

#copying dictionaries
band2=band.copy()
band2["drums"]= "dave"
print(band)
print(band2)

#with constructor function
band3= dict(band)
band3["lagos"]="Ikeja"
del band3["guitar"]
print(band3)
print(' ')

#Nested Dictionaries
member1= {"name":"plant", "instrument": "vocals"
}
member2= {"name":"page", "instrument": "guitar"
}
band={"member1":member1,
      "member2":member2
}
print(band)
print(band["member1"]["instrument"])
print('')
print('')
print('')
print('')

#sets
nums = {1,2,3,4,5}
nums2 = set((1,2,3,4,5))       #constructor functions
print(nums)
print(nums2)
print(type(nums))
print(len(nums))

#no duplicates allowed
nums= {True, 1,2,False,0,2,3,4}     #true is a duplicate of 1, False is a duplicate of 0
print(nums)

#check if a value exsist in a set.
print(2 in nums)

#adding a value/elements to a set.
nums.add(8)
print(nums)

# adding elements from one set to another
morenums={5,6,7}
nums.update(morenums)
print(nums)

#merge sets  to form a new set
one = {1, 2, 3,}
two = {3, 4, 5,}
mynewset= one.union(two)
print(mynewset)

#keep duplicates in  a set.
one = {1, 2, 3,}
two = {2, 3, 5,}
one.intersection_update(two)
print(one)

#keep everything except duplicates in  a set.
one = {1, 2, 3,}
two = {2, 3, 4, 5,}
one.symmetric_difference_update(two)
print(one)