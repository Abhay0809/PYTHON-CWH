'''Author: Abhay Anand'''
# Question 1
'''
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))

if(num1>num4):
    f1 = num1
else:
    f1 = num4

if(num2>num3):
    f2 = num2
else:
    f2 = num3

if(f1>f2):
    print(str(f1) + " is greatest")
else:
    print(str(f2) + " is greatest")
'''

# Question 2
'''
sub1 = int(input("Enter first subject marks\n"))
sub2 = int(input("Enter second subject marks\n"))
sub3 = int(input("Enter third subject marks\n"))

if(sub1<33 or sub2<33 or sub3<33):
    print("You are fail because you have less than 33% in one of the subjects")
elif(sub1+sub2+sub3)/3 < 40:
    print("You are fail due to total percentage less than 40")
else:
    print("Congatulations! You passed the exam")
'''

# Question 3
'''
text = input("Enter the text\n")

if("make a lot of money" in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("click this" in text):
    spam = True
elif("subscribe this" in text):
    spam = True
else:
    spam = False

if(spam):
    print("This text is spam")
else:
    print("This text is not spam")
'''

# Question 4
'''
name = input("Enter your Username: ")
if len(name) < 10:
    print("Username contains less than 10 characters")
else:
    print("Username contains more than 10 characters")
'''

# Question 5
'''
names = ["harry", "shubham", "rohit", "rohan", "aditi", "shipra"]
name = input("Enter the name to check\n")

if name in names:
    print("Your name is present in the list")
else:
    print("Your name is not present in the list")
'''

# Question 6
'''
marks = int(input("Enter Your Marks\n"))

if marks>=90:
    grade = "Ex"
elif marks>=80:
    grade = "A"
elif marks>=70:
    grade = "B"
elif marks>=60:
    grade = "C"
elif marks>=50:
    grade = "D" 
else:
    grade = "F"

print("Your grade is " + grade)
'''

# Question 7
post = input("Enter the post : ")
find_value = "abhay"
if post.find(find_value) == -1:
    print("Not Present")
else:
    print("Abhay is present in post")