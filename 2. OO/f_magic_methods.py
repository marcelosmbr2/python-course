# Magic Methods
# Magic methods, also known as dunder methods (double underscore), are special methods in Python that allow you to define the behavior of your objects for built-in operations
# They enable you to customize how your objects interact with operators, built-in functions, and other language features

class Point:

    # __init__ is a magic method that initializes the object
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # __str__ is a magic method that defines the string representation of the object
    def __str__(self):
        return f"Point({self.x}, {self.y})"

    # __repr__ is a magic method that defines the official string representation of the object
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    # __add__ is a magic method that defines the behavior of the + operator
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

# Creating instances of the Point class
p1 = Point(1, 2)
p2 = Point(3, 4)

# Using magic methods
print(p1)  # Output: Point(1, 2)
print(repr(p1))  # Output: Point(1, 2)
print(p1 + p2)  # Output: Point(4, 6)