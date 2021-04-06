computorChoice = "scissors"
userChoice = input("Rock Paper Scissors!\n")

tieMessage = "TIE!"
winMessage = "You Win!!"
loseMessage = "Loser! Loser!"

if computorChoice == userChoice:
    print(tieMessage)
elif userChoice == "rock" and computorChoice == "scissors":
    print(winMessage)
elif userChoice == "paper" and computorChoice == "rock":
    print(winMessage)
elif userChoice == "scissors" and computorChoice == "paper":
    print(winMessage)
else:
    print(loseMessage)
