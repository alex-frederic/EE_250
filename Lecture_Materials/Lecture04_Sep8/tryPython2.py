# Step 1: Define a Rectangle class
class Rectangle:
    # Class variable: Keeps track of how many rectangles have been created
    rectangle_count = 0
    
    def __init__(self, width, height):
        """
        Constructor to initialize width and height of the rectangle.
        """
        self.width = width  # Instance variable for width
        self.height = height  # Instance variable for height
        
        # Increment the rectangle count whenever a new rectangle is created
        Rectangle.rectangle_count += 1
        print(f"Rectangle created with width={width} and height={height}.")
    
    def area(self):
        """
        Instance method to calculate the area of the rectangle.
        """
        area = self.width * self.height
        print(f"Calculating area: {self.width} * {self.height} = {area}")
        return area
    
    def perimeter(self):
        """
        Instance method to calculate the perimeter of the rectangle.
        """
        perimeter = 2 * (self.width + self.height)
        print(f"Calculating perimeter: 2 * ({self.width} + {self.height}) = {perimeter}")
        return perimeter
    
    @classmethod
    def get_rectangle_count(cls):
        """
        Class method to get the total number of rectangles created.
        """
        print(f"Total rectangles created: {cls.rectangle_count}")
        return cls.rectangle_count


# Step 2: Define a Circle class
import math

class Circle:
    # Class variable: Keeps track of how many circles have been created
    circle_count = 0
    
    def __init__(self, radius):
        """
        Constructor to initialize the radius of the circle.
        """
        self.radius = radius  # Instance variable for radius
        
        # Increment the circle count whenever a new circle is created
        Circle.circle_count += 1
        print(f"Circle created with radius={radius}.")
    
    def area(self):
        """
        Instance method to calculate the area of the circle.
        """
        area = math.pi * self.radius**2
        print(f"Calculating area: π * {self.radius}^2 = {area:.2f}")
        return area
    
    def circumference(self):
        """
        Instance method to calculate the circumference of the circle.
        """
        circumference = 2 * math.pi * self.radius
        print(f"Calculating circumference: 2 * π * {self.radius} = {circumference:.2f}")
        return circumference
    
    @classmethod
    def get_circle_count(cls):
        """
        Class method to get the total number of circles created.
        """
        print(f"Total circles created: {cls.circle_count}")
        return cls.circle_count


# Step 3: Demonstrate how to use these classes
if __name__ == "__main__":
    print("Creating two rectangles...")
    rect1 = Rectangle(4, 5)  # Rectangle with width 4, height 5
    rect2 = Rectangle(10, 3)  # Rectangle with width 10, height 3
    
    print("\nCalculating properties of rectangles:")
    print(f"Area of rect1: {rect1.area()}")
    print(f"Perimeter of rect1: {rect1.perimeter()}")
    print(f"Area of rect2: {rect2.area()}")
    print(f"Perimeter of rect2: {rect2.perimeter()}")
    
    print("\nGetting total rectangles created:")
    Rectangle.get_rectangle_count()
    
    print("\nCreating two circles...")
    circle1 = Circle(3)  # Circle with radius 3
    circle2 = Circle(7)  # Circle with radius 7
    
    print("\nCalculating properties of circles:")
    print(f"Area of circle1: {circle1.area()}")
    print(f"Circumference of circle1: {circle1.circumference()}")
    print(f"Area of circle2: {circle2.area()}")
    print(f"Circumference of circle2: {circle2.circumference()}")
    
    print("\nGetting total circles created:")
    Circle.get_circle_count()
