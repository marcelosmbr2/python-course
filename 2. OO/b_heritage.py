# Heritage

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Class Student that inherits from Person

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Call the constructor of the parent class
        self.student_id = student_id

    def say_hello(self):
        super().say_hello()  # Call the say_hello method of the parent class
        print(f"I am a student with ID: {self.student_id}")

# Creating an instance of the Student class

student1 = Student("Bob", 20, "S12345")
student1.say_hello()