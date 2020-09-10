from abc import ABC
import math

class shape(ABC):

    #abstract method
    def no_of_sides(self):
        pass

    #abstract method
    def calculate_area(self):
        pass

    #abstract method
    def calculate_perimeter(self):
        pass
    

class rectangle(shape):

    #overriding abstract method
    def no_of_sides(self, length, breadth):
        self.length = length
        self.breadth = breadth
        
    def calculate_area(self):
        print("Area of a rectangle is ", self.length * self.breadth)

    def calculate_perimeter(self):
        print("Perimeter of a rectangle is ", 2 * (self.length + self.breadth))

class square(shape):
    
    #overriding abstract method
    def no_of_sides(self, side):
        self.side = side
        
    def calculate_area(self):
        print("Area of a square is ", self.side ** 2)

    def calculate_perimeter(self):
        print("Perimeter of a square is ", 4 * (self.side))

class circle(shape):
    
    #overriding abstract method
    def no_of_sides(self, radius):
        self.radius = radius
        
    def calculate_area(self):
        print("Area of a circle is ", (22/7) * self.radius ** 2)
 
    def calculate_perimeter(self,):
        print("Perimeter of a cirle is ", 2 * (22/7) * self.radius)

class ellipse(shape):
    
    #overriding abstract method
    def no_of_sides(self, minorAxis, majorAxis):
        self.minorAxis = minorAxis
        self.majorAxis = majorAxis    
        
    def calculate_area(self):
        print("Area of a ellipse is ",(22/7) * self.minorAxis * self.majorAxis)

    def calculate_perimeter(self):
        print("Perimeter of a ellipse is ",2 * 3.14 * math.sqrt((self.minorAxis ** 2 + self.majorAxis ** 2)))

obj = rectangle()
obj.no_of_sides(10,20)
obj.calculate_area()
obj.calculate_perimeter()

obj1 = square()
obj1.no_of_sides(20)
obj1.calculate_area()
obj1.calculate_perimeter()

obj2 = circle()
obj2.no_of_sides(10)
obj2.calculate_area()
obj2.calculate_perimeter()

obj3 = ellipse()
obj3.no_of_sides(10,20)
obj3.calculate_area()
obj3.calculate_perimeter()




