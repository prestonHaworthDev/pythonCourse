import random

computerChoice = random.choice(["rock","paper","scissors"])
userChoice = input("Rock Paper Scissors!\n")

tieMessage = "TIE!"
winMessage = "You Win!!"
loseMessage = "Loser! Loser!"

if computerChoice == userChoice:
    print("The computer had " + computerChoice)
    print(tieMessage)
elif userChoice == "rock" and computerChoice == "scissors":
    print("The computer had " + computerChoice)
    print(winMessage)
elif userChoice == "paper" and computerChoice == "rock":
    print("The computer had " + computerChoice)
    print(winMessage)
elif userChoice == "scissors" and computerChoice == "paper":
    print("The computer had " + computerChoice)
    print(winMessage)
else:
    print("The computer had " + computerChoice)
    print(loseMessage)
