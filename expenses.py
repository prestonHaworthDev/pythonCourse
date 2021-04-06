total = 0
expenses = []
n = int(input("How many expenses?\n"))

for i in range(n):
    expenses.append(float(input("Enter an expense: ")))

total = sum(expenses)

print("You spent $", total, sep="")

for x in expenses:
    total = total+x