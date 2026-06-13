# Class Person 

class Person:
    # Constructor method to initialize the attributes of the class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method to display a greeting message
    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating an instance of the Person class

person1 = Person("Alice", 30)
person1.say_hello()   

    