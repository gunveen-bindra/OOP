# Defining base class "Shape".
class Shape:

    # Function to  initialize data members.
    def _getdata(self, length, breadth):
        self._length = int(input("Enter the Length: "))
        self._breadth = int(input("Enter the Breadth: "))


# Defining derived class "Rectangle".
class Rectangle(Shape):

    # Function to calculate area of rectangle.
    def Calculate_area(self):
        self.area = self._length * self._breadth

        print("Area of a rectangle is ", self.area)

# Creating object.
obj = Rectangle()

# Calling function to get the input.
obj._getdata(10, 20)

# Calling function to get the area of a rectangle.
obj.Calculate_area()
