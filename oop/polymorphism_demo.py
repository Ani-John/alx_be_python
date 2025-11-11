import math

# Base class
class Shape:
    def area(self):
        """Method to be overridden by subclasses"""
        raise NotImplementedError("Subclasses must implement this method")

# Derived class - Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Calculate area of a rectangle"""
        return self.length * self.width

# Derived class - Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate area of a circle"""
        return math.pi * (self.radius ** 2)
