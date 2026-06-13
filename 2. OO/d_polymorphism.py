# Polymorphism
# Polymorphism is the ability of different classes to be treated as instances of the same class through a common interface
# It allows you to use a single function or method to work with different types of objects, as long as they implement the required interface

class Dog:
    def speak(self):
        return "Woof!"
    
class Cat:
    def speak(self):
        return "Meow!"

# A function that takes an object that implements the speak method
def animal_sound(animal):
    print(animal.speak())

# Creating instances of the classes
dog1 = Dog()
cat1 = Cat()

# Calling the function with different objects
animal_sound(dog1)  # Output: Woof!
animal_sound(cat1)  # Output: Meow!