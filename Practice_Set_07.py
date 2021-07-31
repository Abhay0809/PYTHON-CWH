'''
Author: Abhay Anand
'''

# Question 1
'''
num = int(input("Enter the number"))
for i in range(1, 11):
    # print(str(num) + " X " + str(i) + "=" + str(i*num))
    print(f"{num}X{i}={num*i}")
'''

# Question 2
'''
l1 = ["Harry", "Sohan", "Sachin", "Rahul"]

for name in l1:
    if name.startswith("S"):
        print("Hello " + name)
'''

# Question 3
'''
num = int(input("Enter the number: "))
i = 1
while i < 11:
    print(f"{num}X{i}={num * i}")
    i += 1
'''

# Question 4
'''
num = int(input("Enter the number: "))
prime = True

for i in range(2, num):
    if(num%i == 0):
        prime = False
        break
if prime:
    print("This number is Prime")
else:
    print("This number is not Prime")
'''

# Question 5
'''
num = int(input("Enter the number: "))
sum = 0
i = 1
while i <= num:
    sum += i
    i += 1

print(sum)
'''

# Question 6
'''
num = int(input("Enter the number: "))
factorial = 1
for i in range(1, num+1):
    factorial = factorial * i
print(f"The factorial of {num} is {factorial}")
'''

# Question 7
'''
n = 3
for i in range(3): 
    print(" " * (n-i-1), end="")
    print("*" * (2*i+1), end="")
    print(" " * (n-i-1))
'''

# Question 8
'''
n = 4

for i in range(4):
    print("*" * (i+1))
'''

# Question 9
rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
for i in range(1,rows+1):
    for j in range(1,columns+1):
        if i==1 or i==rows or j==1 or j==columns:
            print("* ",end='')
        else:
            print("  ",end='')
    print()


# Question 10
'''
num = int(input("Enter the number: "))
for i in range(10,0,-1):
    print(f"{num} * {i} = {i*num}")
'''

