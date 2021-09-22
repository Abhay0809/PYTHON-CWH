import random

randNum = random.randint(1, 100)
userGuess = None
guesses = 0

while userGuess != randNum:

    userGuess = int(input("Enter you Guess Here: "))
    guesses += 1

    if userGuess == randNum:
        print("You guessed the number correctly!")
    else:
        if userGuess > randNum:
            print("You guessed it incorrectly. Guess lower value number!")
        else:
            print("You guessed it incorrectly. Guess higher value number!")

print(f"You guess the number in {guesses} tries!")

with open('hiscore.txt', 'r') as f:
    hiscore = int(f.read())

if guesses < hiscore:
    print(f"You just broke the hiscore of {hiscore} and you are on top now!")
    with open('hiscore.txt', 'w') as f:
        f.write(str(guesses))