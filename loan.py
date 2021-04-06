
# get the loan details
debt = float(input("How many dollars you owe? $"))
apr = float(input("What is your APR? "))
monthlyPayment = float(input("How much you pay a month? $"))
monthCount = int(input("How many months? "))

# calc interest
apr = apr/100/12

for i in range(monthCount):
    # apply interest
    interest = debt*apr
    debt += interest

    if(debt - monthlyPayment < 0):
        print("The last payment is", debt)
        print("You payed off the loan in", i+1, "months!")
        break

    # make payment
    debt -= monthlyPayment

    # print results
    print("Payed", monthlyPayment, "of which", interest, "was interest.", end=' ')
    print("Now I owe", debt)