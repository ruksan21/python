# abstraction
from abc import ABC, abstractmethod
class car (ABC):
    @abstractmethod
    def start_engine(self):
        pass
    
class ford(car):
    def display_name():
        print ("ford car")

class ford(car):
    def start_engine():
        print("Ford engine started")
    
    def display_name():
        print("This is a Ford car")


class bikes:
    def colour():
        return"The bike is red"

    def model():
        return"The bike model is XYZ"
    def _engine():
        return("250cc engine")
        

# Example usage

bikes = bikes()
bikes.display_name()
bikes.colour()
bikes.model()
bikes._engine()