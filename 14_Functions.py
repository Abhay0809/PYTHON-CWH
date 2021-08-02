def percent(marks):
    p = ((marks[0] + marks[1] + marks[2] + marks[3]) / 400) * 100
    return p


marks1 = [45, 78, 86, 77]
percentage1 = percent(marks1)

marks2 = [75, 98, 88, 78]
percentage2 = percent(marks2)


# print(percentage1, percentage2)

def greet(name):
    print("Good Day, " + name)


def mySum(num1, num2):
    return num1 + num2


# greet("Abhay")

s = mySum(6, 32)


# print(s)


def greet2(name="Stranger"):
    print("Good Day, " + name)


# greet2("Abhay")
# greet2()

# RECURSION

# n! = 1 * 2 * 3 * 4...*n
# n! = [1 * 2 * 3 * 4... n-1] *n
# n! = n * (n-1)!

# n = 0
# product = 1
# for i in range(n):
#     product = product * (i+1)
# print(product)

def factorial_iter(n):
    product = 1
    for i in range(n):
        product = product * (i + 1)
    return product


def factorial_recursive(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial_recursive(n - 1)


# f = factorial_iter(5)
f = factorial_recursive(0)
print(f)
