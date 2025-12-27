from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def description(self):
        pass
    
    def display(self):  # Concrete method
        return f"{self.description()}: area = {self.area():.2f}"
