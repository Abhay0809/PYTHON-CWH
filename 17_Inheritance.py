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

