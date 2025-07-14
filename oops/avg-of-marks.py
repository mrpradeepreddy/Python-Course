class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print(sum/3)
s1=Student("ram",[98,97,96])
s1.get_avg()
s1.name="ra"
