class Shape:
    def __init__(self, sides):
        self.sides = sides

    def getArea(self):
        pass


class Rectangle(Shape):

    # initializer
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.sides = 4
        super().__init__(self.sides)

    # method to calculate Area
    def getArea(self):
        return (self.width * self.height)


class Circle(Shape):
    # initializer
    def __init__(self, radius=0):
        self.radius = radius
        self.sides = 0
        super().__init__(self.sides)

    # method to calculate Area
    def getArea(self):
        return (self.radius * self.radius * 3.142)

    def __add__(self):
        temp = Circle()
        return temp


shapes = [Rectangle(6, 10), Circle(7)]
print("Area of rectangle is:", str(shapes[0].getArea()))
print("Area of circle is:", str(shapes[1].getArea()))
print()
