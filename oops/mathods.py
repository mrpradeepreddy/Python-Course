class Student:
    college="ABC"
    name="NONE"
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def welcome(self):
        print("Welcome to college")
    def get_marks(self):
        return self.marks
s1=Student("ram",97)
s1.welcome()
print(s1.get_marks())