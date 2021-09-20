"""
Practice Set 10 : OOPs
"""

'''
class Programmer:
    company = "Microsoft"

    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(f"The name of the {self.company} programmer is {self.name} and the product is {self.product}")


abhay = Programmer("Abhay", "Google")
suman = Programmer("Suman", "Facebook")
abhay.getInfo()
suman.getInfo()
'''

'''
class Calculator:
    def __init__(self, num):
        self.number = num

    def square(self):
        print(f"The value of {self.number} square is {self.number **2}")

    def squareRoot(self):
        print(f"The value of {self.number} square root is {self.number **0.5}")

    def cube(self):
        print(f"The value of {self.number} cube is {self.number **3}")
        
    @staticmethod
    def greet():
        print("-------Welcome to the best calculator of the world-----")

a = Calculator(9)
a.greet()
a.square()
a.squareRoot() 
a.cube()
'''

'''
class Sample:
    a = "Harry"

obj = Sample()
obj.a = "Abhay"
# Sample.a = "Abhay"

print(Sample.a)
print(obj.a)
'''

'''
class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print("************")
        print(f"The name of the train is {self.name}")
        print(f"The seats available in the train are {self.seats}")
        print("************")

    def fareInfo(self):
        print(f"The price of the ticket is: Rs {self.fare}")

    def bookTicket(self):
        if(self.seats>0):
            print(f"Your ticket has been booked! Your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Sorry this train is full! Kindly try in tatkal")

    def cancelTicket(self, seatNo):
        pass

intercity = Train("Intercity Express: 14015", 90, 2)
intercity.getStatus() 
intercity.bookTicket()
intercity.bookTicket()
intercity.bookTicket()
intercity.getStatus()
'''


class Sample:
    def __init__(slf, name):
        slf.name = name


obj = Sample("Harry")
print(obj.name)

