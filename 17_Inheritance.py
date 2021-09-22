"""
Inheritance
"""

'''class Employee:
    company = "Google"

    def showDetails(self):
        print("This is an employee")


class Programmer(Employee):
    language = "Python"

    # company = "Youtube"

    def getLanguage(self):
        print(f"The language is {self.language}")

    def showDetails(self):
        print("This is an programmer")


e = Employee()
e.showDetails()
p = Programmer()
p.showDetails()
print(p.company)'''

# Types of Inheritance

# Single Inheritance
'''
class Employee:
    company = "Google"

    def showDetails(self):
        print("This is an employee")

class Programmer(Employee):
    language = "Python"
    # company = "Youtube"

    def getLanguage(self):
        print(f"The language is {self.language}")
    
    def showDetails(self):
        print("This is an programmer")


e = Employee()
e.showDetails()
p = Programmer()
p.showDetails()
print(p.company)
'''

# Multiple Inheritance
'''
class Freelancer:
    company = "Fiverr"
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 1

class Employee:
    company = "Visa"
    eCode = 120


class Programmer(Freelancer, Employee):
    name = "Rohit"

p = Programmer()
p.upgradeLevel()
print(p.company)
'''

# Multi-Level Inheritance
'''
class Person:
    country = "India"
    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    company = "Honda"

    def getSalary(self):
        print(f"Salary is {self.salary}")
    
    def takeBreath(self):
        print("I am an Employee so I am luckily breathing..")

class Programmer(Employee):
    company = "Fiverr"
    
    def getSalary(self):
        print(f"No salary to programmers")
    
    def takeBreath(self):
        print("I am a Progarmmer so I am breathing++..")

p = Person()
p.takeBreath()
# print(p.company) # throws an error

e = Employee()
e.takeBreath()
print(e.company)

pr = Programmer()
pr.takeBreath()
print(pr.company)
print(pr.country)
'''

# Super Method
'''
class Person:
    country = "India"

    def __init__(self):
        print("Initializing Person...\n")

    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    company = "Honda"

    def __init__(self):
        super().__init__()
        print("Initializing Employee...\n")

    def getSalary(self):
        print(f"Salary is {self.salary}")
    
    def takeBreath(self):
        super().takeBreath()
        print("I am an Employee so I am luckily breathing..")

class Programmer(Employee):
    company = "Fiverr"

    def __init__(self):
        # super().__init__()
        print("Initializing Programmer...\n")

    def getSalary(self):
        print(f"No salary to programmers")
    
    def takeBreath(self):
        super().takeBreath()
        print("I am a Progarmmer so I am breathing++..")

# p = Person()
# p.takeBreath() 

# e = Employee()
# e.takeBreath() 

pr = Programmer()
# pr.takeBreath() 
'''

# Class Method
'''
class Employee:
    company = "Camel"
    salary = 100
    location = "Delhi"

    # def changeSalary(self, sal):
    #     self.__class__.salary = sal

    @classmethod
    def changeSalary(cls, sal):
        cls.salary = sal

e = Employee()
print(e.salary)
e.changeSalary(455)
print(e.salary)
print(Employee.salary)
'''

# Property decorator
'''
class Employee:
    company = "Bharat Gas"
    salary = 5600
    salarybonus = 400
    # totalSalary = 6100

    @property
    def totalSalary(self):
        return self.salary + self.salarybonus

    @totalSalary.setter
    def totalSalary(self, val):
        self.salarybonus = val - self.salary

e = Employee()
print(e.totalSalary)
e.totalSalary = 5800
print(e.salary)
print(e.salarybonus)
'''

# Operator Overloading
'''
class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2):
        print("Lets add")
        return self.num + num2.num

    def __mul__(self, num2):
        print("Lets multiply")
        return self.num * num2.num

n1 = Number(4)
n2 = Number(6)
sum = n1 + n2
mul = n1 * n2
print(sum)
print(mul)
'''


# Other Dunder Methods
class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2):
        print("Lets add")
        return self.num + num2.num

    def __mul__(self, num2):
        print("Lets multiply")
        return self.num * num2.num

    def __str__(self):
        return f"Decimal Number: {self.num}"

    def __len__(self):
        return 1


n = Number(9)
print(n)
print(len(n))
