# Program on Multilevel Inheritance

class Student:
    
    def acceptData(self):
        self.rollno = int(input("Enter Rollno:"))
        self.name = str(input("Enter Name: "))
        self.class_ = str(input("Enter Class: "))
        self.div = str(input("Enter Div: "))
        self.sem = input("Enter Semester : ")

class Marks(Student):
    
    def accept_marks(self):
        self.ip = int(input("Enter imperative programming marks: "))
        self.wp = int(input("Enter  web programming marks: "))
        self.de = int(input("Enter digital electronics marks: "))
        self.os = int(input("Enter operating system marks: "))
        self.dm = int(input("Enter discrete mathematics marks: "))
        self.cs = int(input("Enter communocation skills marks: "))


class Result(Marks):
    
    def calculate(self):
        self.total = self.ip + self.wp + self.de + self.os + self.dm + self.cs
        self.avg = self.total/6
        self.percentage = (self.total * 100)/600
        print("\nTotal marks:",self.total)
        print("Average marks:",self.avg)
        print("Percentage:",self.percentage)

c=Result()
c.acceptData()
c.accept_marks()                     
c.calculate()
