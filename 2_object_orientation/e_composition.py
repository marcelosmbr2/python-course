# Composition
# In composition, one class contains an instance of another class as a part of its state

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

class Car:
    def __init__(self, make, model, year, engine):
        self.make = make
        self.model = model
        self.year = year
        self.engine = engine

    def start_engine(self):
        print(f"{self.year} {self.make} {self.model} engine started with {self.engine.horsepower} horsepower.")

# Creating instances of the classes
engine1 = Engine(200)
car1 = Car("Toyota", "Camry", 2020, engine1)

# Calling the method
car1.start_engine()  # Output: 2020 Toyota Camry engine started with 200 horsepower.