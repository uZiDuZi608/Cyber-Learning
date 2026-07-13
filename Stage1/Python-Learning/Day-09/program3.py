import art
x=art.logo
print(x)
bidding_record={}
more=""
highest_bid=0
winner=""

while more!="no":
    name=input("What is your name? ")
    price=int(input("How  much you want to bid? $"))
    bidding_record[name]=price
    more=input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()   
    print("\n" * 20)
for name in bidding_record:
        if bidding_record[name]>highest_bid:
            highest_bid=bidding_record[name]
            winner=name

print(f"The winner is {winner} with a bid of ${highest_bid}.")