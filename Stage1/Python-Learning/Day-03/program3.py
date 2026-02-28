print("Welcome to Python Pizza Deliveries")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni? Y or N: ")
cheese = input("Do you want extra cheese? Y or N: ")
bill = 0
if size == "s" or size == "S" :
    bill += 15
elif size == "m" or size == "M":
    bill += 20
elif size == "l" or size == "L":
    bill += 25
else:
    print("Invalid size selected.")
    exit()
if pepperoni == "y" or pepperoni == "Y":
    if size == "s" or size == "S":
        bill += 2
    else:
        bill += 3
if cheese == "y" or cheese == "Y":
    bill += 1
print(f"Your total bill is ${bill}")