class Number:
    def sum(self):
        return self.a + self.b


num = Number()
num.a = 8
num.b = 26
s = num.sum()
# print(s)

# a = 8
# b = 26

# print("The sum of a and b is ", a+b)

# Railways OOPs Example

'''
import pandas as pd

pd.DataFrame()
class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

abhaysApplication = RailwayForm()
abhaysApplication.name = "Abhay"
abhaysApplication.train = "Rajdhani Express"
abhaysApplication.printData()
'''

# Game Example

'''
class Remote():
    pass

class Player:
    def moveRight(self):
        pass

    def moveLeft(self):
        pass

    def moveTop(self):
        pass

remote1 = Remote()
player1 = Player()

if(remote1.isLeftPressed()):
    player1.moveLeft()
'''


class Employee:
    company = "Google"
    salary = 100


abhay = Employee()
suman = Employee()

# Creating instance attribute salary for both the objects
abhay.salary = 300
suman.salary = 400

# print(abhay.salary)
# print(suman.salary)

# print(abhay.company)
# print(suman.company)

Employee.company = "YouTube"


# print(abhay.company)
# print(suman.company)


# Below line throws an error as address is not present in instance/class
# print(suman.address)

class Employee:
    company = "Google"

    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("Good Morning, Sir")

    @staticmethod
    def time():
        print("The time is 9AM in the morning")


abhay = Employee()
abhay.salary = 100000

# abhay.getSalary("Thanks!")  # Employee.getSalary(harry)
# abhay.greet()  # Employee.greet()
# abhay.time()
# abhay.getSalary()  # Employee.getSalary(abhay)



