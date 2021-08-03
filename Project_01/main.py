import random

print("ROCK(🪨) - PAPER(📃) - SCISSOR(✂️)")
print("         - Coded by Abhay Anand")
print("-------------------------------")

rounds = int(input("Enter Number of Rounds: "))
print("---------------------------")

options = ['r', 'p', 's']

round = 1
comp_win = 0
user_win = 0

while round <= rounds:
    # Round Display
    print(f"\nRound : {round}\nRock : 'r'\t|| Paper : 'p'\t|| Scissor : 's'")

    # Exceptional Handling
    try:
        player = input("\nChoose you option: ")
    except EOFError as e:
        print(e)

    # Validation Check
    if player != 'r' and player != 'p' and player != 's':
        print("Invalid Input entered, Try Again.\n")
        continue

    # randomly choose item from list- options
    computer = random.choice(options)

    # Conditions based on the game rule
    if computer == 'r':
        if player == 'p':
            user_win += 1
        elif player == 's':
            comp_win += 1

    elif computer == 'p':
        if player == 's':
            user_win += 1
        elif player == 'r':
            comp_win += 1

    elif computer == 's':
        if player == 'r':
            user_win += 1
        elif player == 'p':
            comp_win += 1

    # Winner Decision
    if user_win > comp_win:
        print(f"You Won Round {round}")
        print("---------------------------")
    elif comp_win > user_win:
        print(f"Computer Won Round: {round}")
        print("---------------------------")
    else:
        print("Draw, Retry Again!! ")
        print("---------------------------")

    round += 1

# Final Winner decision on the basis of won
if user_win > comp_win:
    print("Congratulations!! You Won 🎉")
elif comp_win > user_win:
    print("You lose!! ☹️")
else:
    print("Match Drawn!! 😐")
