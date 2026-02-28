import random

rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper='''
    _______
---'   ____)____
          ______)
          _______)
          _______)
---.__________)
'''
scissors='''
    _______
---'   ____)____
          ______)
        __________)
      (____)
---.__(___)
'''
x=["rock","paper","scissors"]
y=random.randint(0,2)
z=(x[y])
user=(input("what do you choose rock,paper,scissor ?\ntype 0 for rock\ntype 1 for paper\ntype 2 for scissors\n"))
if user=='0':
    print(rock)
    if z=='paper':
        print(f"computer chose:{paper}")
        print("you lose")
    elif z=='scissors':
        print(f"computer chose:{scissors}")
        print("you win")
    else:
        print(f"computer chose:{rock}")
        print("draw")
elif user=='1':
    print(paper)
    if z=='rock':
        print(f"computer chose:{rock}")
        print('you  win')
    elif z=='scissors':
        print(f"computer chose:{scissors}")
        print('you lose')
    else:
        print(f"computer chose:{paper}")
        print('draw')
elif user=='2':
    print(scissors)
    if z=='rock':
        print(f"computer chose:{rock}")
        print('you lose')
    elif z=='paper':
        print(f"computer chose:{paper}")
        print('you win')
    else:
        print(f"computer chose:{scissors}")
        print('draw')
else:
    print('invalid input')
