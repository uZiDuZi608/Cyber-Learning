print("welcome to the rollercoaster")
height=int(input("what is you height in cm? "))
bill=0
if height>=120:
    print("you can ride the rollercoaster")
    age = int(input("what is your age? "))
    if age<=5:
        print("child tickets are 5$")
        bill=5
    elif age<=12:
        print("youth tickets are 7$")
        bill=7
    else:
        print("adult tickets are 12$")
        bill=12
    photo=(input("do you want to take a photo? type y for yes or n for no "))
    if photo=="y" or photo=="Y":
        bill+=3
    print(f"your final bill is ${bill}")


else:
    print("sorry you have to grow taller before you can ride")