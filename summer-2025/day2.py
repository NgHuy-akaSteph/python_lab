import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius  # bcd

    def area(self):
        return math.pi * self.radius**2  # abc

    def perimeter(self):
        return 2 * math.pi * self.radius


if __name__ == "__main__":
    shapes = []

    n = int(input("Enter number of shapes: "))
    for _ in range(n):
        inp = input()
        if len(inp.split()) == 2:
            w, h = map(float, inp.split())
            shapes.append(Rectangle(w, h))
        elif len(inp.split()) == 1:
            r = float(inp)
            shapes.append(Circle(r))
        else:
            print("Invalid input format")

    shapes = sorted(shapes, key=lambda x: x.area())
    print(shapes[-1].area())
