temp = int(input("What is the temperature outside?\n"))

if temp > 80:
    print("too hot yo")
elif temp < 60:
    print("too cold yo")
else:
    print("It's nice out there")

if temp > 80 or temp < 60:
    print("Stay inside!")
else:
    print("GTFO")