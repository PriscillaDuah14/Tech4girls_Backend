class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @property
    def area(self):
        return self.length * self.width

    @property
    def perimeter(self):
        return 2 * (self.length + self.width)

    def __str__(self):
        return f"Rectangle(Length: {self.length}, Width: {self.width})"

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.area == other.area
        return False

# Creating two rectangle instances
rectangle1 = Rectangle(5, 3)
rectangle2 = Rectangle(6, 2)

# Demonstrating the use of all methods
print(rectangle1) 
print(f"Area of rectangle1: {rectangle1.area}")  
print(f"Perimeter of rectangle1: {rectangle1.perimeter}")  

print(rectangle2)  
print(f"Area of rectangle2: {rectangle2.area}")  
print(f"Perimeter of rectangle2: {rectangle2.perimeter}")  

# Comparing the two rectangles
area_equal = rectangle1 == rectangle2
print(f"Area of rectangle1 and rectangle2 equal in area {area_equal}")  
