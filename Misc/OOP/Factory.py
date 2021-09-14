from abc import ABC, abstractmethod
from enum import Enum

class ShapeTypes(Enum):
    circle, rectangle, square = 1,2,3


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
    @abstractmethod
    def calculate_perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_area(self):
        return self.height * self.width

    def calculate_perimeter(self):
        return 2 * (self.height + self.width)

class Square(Shape):
    def __init__(self, width):
        self.width = width

    def calculate_area(self):
        return self.width ** 2

    def calculate_perimeter(self):
        return 4 * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius

class ShapeFactory():
    def createShape(self,name):
        if name == "circle":
            return Circle(1)
        elif name == "sqaure":
            pass

        elif name == "rectangle":
            pass

factory = ShapeFactory
shape1 = ShapeFactory.createShape('',"circle")
print(type(shape1))