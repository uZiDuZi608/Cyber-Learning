def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Encounter an error:")
def addition(a,b):
    """this is a function that adds two numbers

    Args:
        a (int): _description_
        b (int): _description_
    """
    return(a+b)
def subtraction(a,b):
    """this is a funtion that sutracts two numbers

    Args:
        a (_int): _description_
        b (int): _description_
    """
    return(a-b)
def multiplication(a,b):
    """this is a function that multiplies two numbers

    Args:
        a (int): _description_
        b (int): _description_
    """
    return(a*b)
def division(a,b):
    """this is a function that divides two numbers

    Args:
        a (_type_): _description_
        b (_type_): _description_
    """
    if b == 0: return "error: cannot divide by zero!"
    return a / b

x = get_int_input("Enter value for variable 1: ")
y = get_int_input("Enter value for variable 2: ")
z = get_int_input("Enter number for selection:\n1 for addition\n2 for subtraction\n3 for multiplication\n4 for division\n")
if z==1:
    print(addition(x,y))
elif z==2:
    print(subtraction(x,y))
elif z==3:
    print(multiplication(x,y))
elif z==4:
    print(division(x,y))
else:
    print("invalid input")