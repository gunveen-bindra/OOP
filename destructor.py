# Program to show destructor


class Person:
    def __init__(self, fname, lname):
        print("creates and initialize the instance of person class")
        self.fname = fname
        self.lname = lname

    def getFullName(self):
        print(self.fname, " ", self.lname)

    def __del__(self):
        print("destroy instance of person class")


p1 = Person("Rohit", "Sharma")
p1.getFullName()
p2 = Person("Riya", "Sharma")
p2.getFullName()
p1 = None
p2 = None
