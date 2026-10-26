import re
names = ['Philip Daniels' , 'Bolu Meduteni', 'David Akinsanya', 'Bright Gideon', 'Agent 47', 'Josuhu Essien', 'Jethro Otobo', 'Julius Berger', 'Ben' 'Tolu', 'Mimi' ]

#find the people with first and last names only.
regex= '\w+ \w+$'
for name in names:
    result= re.search(regex, name)
    if result:
        print(name)