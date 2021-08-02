# Question 1
def maximum(num1, num2, num3):
    if num1 > num2:
        if num1 > num3:
            return num1
        else:
            return num3
    else:
        if num2 > num3:
            return num2
        else:
            return num3


m = maximum(13, 55, 2)


# print("The value of the maximum is " + str(m))

# Question 2
def farh(cel):
    return (cel * (9 / 5)) + 32


# c = int(input("Enter temperature in celcius: "))
# f = farh(c)
# print("Fahrenheit Temperature is " + str(f))

# Question 3
'''print("Hello", end=" ")
print("How", end=" ")
print("are", end=" ")
print("you?", end=" ")'''


# Question 4
def recSum(n):
    if n <= 1:
        return n
    else:
        return n + recSum(n - 1)


'''num = int(input("Enter Number: "))
if num < 0:
    print("Enter a Positive Number!")
else:
    print(f"Sum of {num} natural number is {recSum(num)}")'''


# Question 5
# n = 3
# for i in range(n):
#     print("*" * (n-i))

# Question 6
def convert(i):
    cm = i * 2.54
    return cm


'''inch = int(input("Enter measurement in inch: "))
print(f"{inch} inch = {convert(inch)} cm")'''


# Question 7
def remove_and_split(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()


this = "     Abhay is a good      "
n = remove_and_split(this, "Abhay")
# print(n)
# print(this)
# print(this.strip())


# Question 8
def table(n):
    for i in range(1,11):
        print(f"{n} * {i} = {n*i}")


num = int(input("Enter the number to get table: "))
table(num)
