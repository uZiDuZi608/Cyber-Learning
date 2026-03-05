import random
letters=[ 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols=['!','#','$','%','&','(',')','*','+']
print("welcome to password generator")
no_letters=int(input("enter the amount of letters you want in your password\n"))
no_numbers=int(input("enter the amount of numbers you want in your password\n"))
no_symbols=int(input("enter the amount of symbol you want in your password\n"))

my_list=[]

for letter in range(no_letters):
    my_list.append(random.choice(letters))
for number in range(no_numbers):
    my_list.append(random.choice(numbers))
for symbol in range(no_symbols):
    my_list.append(random.choice(symbols))
random.shuffle(my_list)
password=''.join(my_list)
print(f"yor password is {password}")