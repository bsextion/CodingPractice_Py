from abc import ABC,abstractmethod
class Shape(ABC):  # Shape is a child class of ABC
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return pow(self.length, 2)

    def perimeter(self):
        return (4 * self.length)



shape = Square()
print(shape.area())
