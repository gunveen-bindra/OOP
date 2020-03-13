# Program to show constructor

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def getFullName(self):
        print(self.fname, " ", self.lname)


p1=Person("Rohit", "Sharma")
p1.getFullName()
p2=Person("Riya", "Sharma")
p2.getFullName()
