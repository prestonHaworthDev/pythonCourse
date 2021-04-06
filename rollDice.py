import random

mini = int(input("What is the lowest number?\n"))
maxi = int(input("What is the highest number?\n"))

roll = random.randint(mini,maxi)

print("The computer rolled a " + str(roll))