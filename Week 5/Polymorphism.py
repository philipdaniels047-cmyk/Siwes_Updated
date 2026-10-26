class French:
    def say_hello(self):
        print("Bonjour")

class Chinese:
    def say_hello(self):
        print("Nǐ hǎo")

def intro(lang):                #function that takes an object as an argument
    lang.say_hello()

#Instances
Philip= French()           #instance of French class
John= Chinese()            #instance of Chinese class   

intro(Philip)
intro(John)    