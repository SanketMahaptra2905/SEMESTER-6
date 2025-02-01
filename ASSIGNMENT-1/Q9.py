print("NAME:- SANKET MAHAPATRA")
print("REGISTRATION NUMBER:- 2241013017")

import math

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

circle = Circle(5)
rectangle = Rectangle(4, 6)

print(f"Circle Area: {circle.area()}")
print(f"Rectangle Area: {rectangle.area()}")

print("\nExplanation: Polymorphism allows different subclasses to override the area() method while maintaining a consistent interface from the base class.\n")
print("Explanation: The Shape class defines a common method, and subclasses provide their own specific implementations for calculating the area.\n")
print("Expanlanation: This simplifies working with different shapes because they can be handled uniformly, making code more flexible and maintainable.\n")
print("Explanation: By using polymorphism, we can call the area() method on any Shape object without worrying about its specific type, improving code reusability.\n")
