# Function Definition

def hello_world():
    print("Hello, World!")

def add(a, b):
    return a + b

def greet(name):
    return f"Hello, {name}!"

# Function Calls

hello_world()  # Output: Hello, World!  
result = add(5, 3)
print(result)  # Output: 8
greeting = greet("Alice")

print(greeting)  # Output: Hello, Alice!

# Function with Default Parameters

def greet(name="Guest"):
    return f"Hello, {name}!"

print(greet())  # Output: Hello, Guest!
print(greet("Bob"))  # Output: Hello, Bob!

# Function with Variable Number of Arguments

def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3))  # Output: 6
print(sum_all(4, 5))     # Output: 9

# Function with Keyword Arguments

def display_info(name, age):
    print(f"Name: {name}, Age: {age}")

display_info("Alice", 30)  # Output: Name: Alice, Age: 30
display_info(age=25, name="Bob")  # Output: Name: Bob, Age: 25

# Lambda Function

square = lambda x: x ** 2
print(square(5))  # Output: 25

# Recursive Function

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120