import random


def getuserchoice():
    while True:
        user_choice = input("Choose rock, paper, or scissors: ")
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")


def getcomchoice():
    return random.choice(['rock', 'paper', 'scissors'])


def getwinner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'scissors' and computer_choice == 'paper') or (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"


user_score = 0
computer_score = 0

while True:
    print("___________________________________________________________________________________________")
    print("\n\t\t\t -------------- ROCK-PAPER-SCISSORS GAME --------------\n")
    user_choice = getuserchoice()
    computer_choice = getcomchoice()

    print("You chose {}. Computer chose {}".format(user_choice,computer_choice))

    result = getwinner(user_choice, computer_choice)
    print(result)

    if result == "You win!":
        user_score += 1
    elif result == "Computer wins!":
        computer_score += 1

    print("Score - You: {}, Computer: {}".format(user_score,computer_score))

    play = input("Do you want to play another round? (yes/no): ").lower()
    if play != "yes":
        print("\nThank you for playing.........!!!")
        break
