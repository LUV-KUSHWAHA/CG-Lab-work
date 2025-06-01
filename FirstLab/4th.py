#Classes and Objects
class Student:
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll

    def display(self):
        print("Name: ",self.name)
        print("Roll No.: ",self.roll)

s1 = Student("Luv", 59)
s1.display()
s2 = Student("Bob", 00)
s2.display()