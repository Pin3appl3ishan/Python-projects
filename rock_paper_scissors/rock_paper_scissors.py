import random

user_wins = 0
computer_wins = 0

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in ["rock", "paper", "scissors"]:
        print("Please enter a valid input")
        continue

    random_number = random.randint(0, 2)
    if random_number == 0:
        computer = "rock"
    elif random_number == 1:
        computer = "paper"
    else:
        computer = "scissors"

    print("Computer chose: " + computer)
    if user_input == computer:
        print("It's a tie!")
    elif user_input == "rock" and computer == "scissors":
        print("You won!")
        user_wins += 1
    elif user_input == "paper" and computer == "rock":
        print("You won!")
        user_wins += 1
    elif user_input == "scissors" and computer == "paper":
        print("You won!")
        user_wins += 1
    else:
        print("You lost!")
        computer_wins += 1