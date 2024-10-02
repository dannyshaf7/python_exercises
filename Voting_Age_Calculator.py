# get age from user and tell them whether they can vote in US elections

age = int(input("Enter your age: "))

if age >= 18:
    print("you can vote")
elif age < 10:
    print("watch Barney")
else:
    print("you cannot vote")
