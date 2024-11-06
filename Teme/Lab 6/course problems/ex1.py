# 1 ------------------------------------------------
# Create a class hierarchy for shapes, starting with a base class Shape.
# Then, create subclasses like Circle, Rectangle, and Triangle.
# Implement methods to calculate area and perimeter for each shape.
import math

class Shape:
    def Print(self):
        print("Shape")

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def calc_area(self):
        return math.pi * pow(self.r, 2)

    def calc_perimeter(self):
        return 2 * math.pi * self.r

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calc_area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def calc_perimeter(self):
        return self.a + self.b + self.c

class Rectangle(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def calc_area(self):
        return self.l * self.w

    def calc_perimeter(self):
        return 2 * (self.l + self.w)


circle = Circle(5)
triangle = Triangle(2, 2, 3)
rectangle = Rectangle(3,4)

circle.Print()
triangle.Print()
rectangle.Print()

print("Circle parameter:", circle.calc_perimeter(), "Circle area:", circle.calc_area())
print("Triangle parameter:", triangle.calc_perimeter(), "Triangle area:", triangle.calc_area())
print("Rectangle parameter:", rectangle.calc_perimeter(), "Rectangle area:", rectangle.calc_area())
