print("Welcome to the tip calculator! ")
x=float(input("whats the total bill? "))
y=float(input("how much tip would you like to give? "))
z=int(input("how many people are splitting the bill "))
total=(x+((y/100)*x))/z
total_split=round(total,2)
print(f"each person should pay is: {total_split}")
