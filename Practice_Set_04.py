# Python program to store seven fruits in list entered by user.
f1 = input("Enter Fruit Number 1: ")
f2 = input("Enter Fruit Number 2: ")
f3 = input("Enter Fruit Number 3: ")
f4 = input("Enter Fruit Number 4: ")
f5 = input("Enter Fruit Number 5: ")
f6 = input("Enter Fruit Number 6: ")
f7 = input("Enter Fruit Number 7: ")

myFruitList = [f1, f2, f3, f4, f5, f6, f7]
print(myFruitList)

# Python program to accept marks of 6 students and display in sorted order.
m1 = int(input("Enter Marks for Student Number 1: "))
m2 = int(input("Enter Marks for Student Number 2: "))
m3 = int(input("Enter Marks for Student Number 3: "))
m4 = int(input("Enter Marks for Student Number 4: "))
m5 = int(input("Enter Marks for Student Number 5: "))
m6 = int(input("Enter Marks for Student Number 6: "))

myList = [m1, m2, m3, m4, m5, m6]
myList.sort()
print(myList)

# Tuple change test
a = (2, 4, 5, 3, 2)
a[0] = 45

# Python program to sum a list with 4 numbers
a = [2, 4, 56, 7]

print(a[0] + a[1] + a[2] + a[3])
print(sum(a))

# Python program to count number of zeros in following tuple
a = (7, 0, 8, 0, 0, 9)
print(a.count(0))