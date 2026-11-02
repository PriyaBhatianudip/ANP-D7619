from abc import ABC, abstractmethod

# to create an abstract class:-
class Shape(ABC):
    @abstractmethod
    def calculateArea(self):
        pass

    @abstractmethod
    def calculatePerimeter(self):
        pass
    # pass keyword can be used to define an empty method or empty class as well
class Rectangle(Shape):
    def calculatePerimeter(self):
        l = int(input("Enter the length of the rectangle: "))
        b = int(input("Enter the width of the rectangle: "))
        print("Perimeter: ",2*(l+b))

    def calculateArea(self):
        l = int(input("Enter the length of the rectangle: "))
        b = int(input("Enter the width of the rectangle: "))
        print("Area : ", l*b)

class Square(Shape):
    def calculateArea(self):
        side = int(input("Enter side length: "))
        print("Area of Square: ", side*side)

    def calculatePerimeter(self):
        side = int(input("Enter side length: "))
        print("Perimeter of Square: ", 4*side)


rect = Rectangle()
sqr = Square()
rect.calculateArea()
rect.calculatePerimeter()
sqr.calculatePerimeter()
sqr.calculateArea()

