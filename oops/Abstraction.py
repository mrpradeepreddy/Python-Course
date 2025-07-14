# hiding unnecessary data
class Car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False
    def Start(self):
        self.acc=True
        self.clutch=True
        print("Car Starts")
car1=Car()
car1.Start()