#creating class

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
s1=Student("ram",97)
print(s1.name,s1.marks)

s2=Student("raju",89)
print(s2.name,s2.marks)