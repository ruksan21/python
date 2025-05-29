from abc import ABC, abstractmethod

# Abstract Class
class Car(ABC):
    @abstractmethod
    def start_engine(self):
        pass

# Concrete Class Implementing Abstract Method
class Ford(Car):
    def start_engine(self):
        print("Ford engine started")
    
    def display_name(self):
        print("This is a Ford car")

# Regular Class without Abstraction
class Bikes:
    def colour(self):
        return "The bike is red"

    def model(self):
        return "The bike model is XYZ"
    
    def _engine(self):
        return "250cc engine"

# Example usage

# Creating an instance of Ford and calling methods
my_car = Ford()
my_car.start_engine()
my_car.display_name()

# Creating an instance of Bikes and calling methods
my_bike = Bikes()
print(my_bike.colour())  
print(my_bike.model())  
print(my_bike._engine())  