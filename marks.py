class marks:
    student_name=str(input("Enter your name: "))
    student_rno=int(input("Enter your roll no: "))
    sclass=input("Enter your class: ")

    def subjects(self):
            self.dbms=int(input("Enter marks in DBMS: "))
            self.pp=int(input("Enter marks in PP: "))
            self.wp=int(input("Enter marks in WP: "))
            self.oop=int(input("Enter marks in OOP: "))
            self.dm=int(input("Enter marks in DM: "))
   
    def internal_mrks(self):
           print("Enter your marks out of 25 for internals: ")
           self.subjects()
           self.int_mrks=self.dbms+self.pp+self.wp+self.oop+self.dm    

    def theory_mrks(self):
        print("Enter your marks out of 75 for theory: ")
        self.subjects()
        self.th_mrks=self.dbms+self.pp+self.wp+self.oop+self.dm
       

    def practicals(self):
        print("Enter your marks out of 50 for practicals: ")
        self.subjects()
        self.pr_mrks=self.dbms+self.pp+self.wp+self.oop+self.dm
        self.mrks=self.int_mrks + self.th_mrks + self.pr_mrks
        self.total=(25*5)+(75*5)+(50*5)
        self.percent= ( self.mrks/ self.total)*100
        self.percentage=round(self.percent)
        
    def grade(self):
        if self.percentage>90:
            print("You pass!")
            print("Your percentage is: ",self.percentage)
            print("O GRADE!")
        elif self.percentage>75:
            print("You pass!")
            print("Your percentage is: ",self.percentage)
            print("A+ GRADE!")
        elif self.percentage>60:
            print("You pass!")
            print("Your percentage is: ",self.percentage)
            print("A GRADE!")
        elif self.percentage>50:
            print("You pass!")
            print("Your percentage is: ",self.percentage)
            print("B+ GRADE!")
        elif self.percentage>45:
            print("You pass!")
            print("Your percentage is: ",self.percentage)
            print("B GRADE!")
        else:
            print("You fail!")
            print("Your percentage is: ",self.percentage)

    def display(self):
        print(self.student_name)
        print(self.sclass)
        print(self.student_rno)
c=marks()
c.internal_mrks()
c.theory_mrks()        
c.practicals()
c.display()
c.grade()







        
        
        
