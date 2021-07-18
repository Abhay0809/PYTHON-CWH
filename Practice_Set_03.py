# Python program to display user entered name along with greeting

name = input("Enter your name: ")
greet = "Good Night"

print(name + greet)

# Template replacement text
letter = '''Dear <|NAME|>,
Greetings from ABC coding house. I am happy to tell you about your selection
You are selected!
Have a great day ahead!
Thanks and regards,
Bill
Date: <|DATE|>
'''

name = input("Enter your name: ")
date = input("Enter your date: ")
letter.replace("<|NAME|>", name)
letter.replace("<|DATE|>", date)
print(letter)

# Python program to detect single and double spaces

sentence = "This line  consists of single space and double  space written by  Abhay Anand!"
print("Single Space", sentence.count(" "))
print("Double Space", sentence.count("  "))

# Use escape sequence

letter = "Dear Abhay, This Python course is nice! Thanks!"
print(letter)
letter_formatted = "Dear Abhay, \n\tThis Python course is nice! \nThanks!"
print(letter_formatted)

