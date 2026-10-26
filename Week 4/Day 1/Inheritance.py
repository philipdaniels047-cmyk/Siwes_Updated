class Animal:
    def __init__(self, name):
        self.name= name
        
    def speak(self):
        return f"{self.name} makes a sound."
    
    ##
class dog(Animal):
    def speak(self):
        return f"{self.name} barks. "
    


# Creating instances
generic_animal = Animal("Generic")
dog = dog("Buddy")

print(generic_animal.speak())  # Output: Generic makes a sound.
print(dog.speak())             # Output: Buddy barks!



# The super() Function
# The super() function allows a child class to call methods from its parent class—most commonly used to invoke the parent's __init__ constructor so shared attributes are properly initialized.

# Python


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        # Delegate name and salary initialization to the parent class
        super().__init__(name, salary)
        self.programming_language = programming_language

dev = Developer("Alice", 90000, "Python")
print(dev.name)                  # Output: Alice
print(dev.programming_language)  # Output: Python