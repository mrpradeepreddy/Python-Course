# methods dont use the self parameter
class Student:
    @staticmethod
    def college():
        print("ABC college")
s1=Student()
s1.college()