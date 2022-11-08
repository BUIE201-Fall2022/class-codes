class Rectangle:
    def __init__(self, height, width) -> None:
        self.height = height
        self.width = width
    
    def print(self):
        for i in range(self.height):
            for j in range(self.width):
                print("*", end="")
            print("")

class Square:
    def __init__(self, dimension) -> None:
        self.dimension = dimension
    
    def print(self):
        for i in range(self.dimension):
            for j in range(self.dimension):
                print("*", end="")
            print("")

class NewSquare(Rectangle):
    def __init__(self, dimension) -> None:
        Rectangle.__init__(self, dimension, dimension)

print("Rectangle:")
rect = Rectangle(10, 15)
rect.print()

print("Square:")
sqr = Square(6)
sqr.print()

print("NewSquare:")
nsqr = NewSquare(10)
nsqr.print()
