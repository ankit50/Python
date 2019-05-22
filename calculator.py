# Defining Functions:
def add(a, b):
    c = a + b
    return c


def sub(a, b):
    c = a - b
    return c


def divide(a, b):
    if b == 0:
        print("Divide By Zero occured!!!!!")
    else:
        c = a / b
        return c


def mul(a, b):
    c = a * b
    return c


# Defining the input from user
choice2 = "Y"
while choice2 == "Y" or choice2 == "y":
    print("*************CALCULATOR DEMO**************")
    print("1.ADDITION\n2.SUBTRACTION\n3.DIVISION\n4.MULTIPLICATION")
    choice = input("ENTER THE OPERATION NUMBER[1-4]")
    num1 = int(input("\nEnter First Number:"))
    num2 = int(input("\nEnter Second Number:"))
    if choice == "1":
        result = add(num1, num2)
        print("\nTHE SUM OF {0} and {1} is {2}".format(num1, num2, result))
    elif choice == "2":
        result = sub(num1, num2)
        print("\nTHE DIFFERENCE OF {0} and {1} is {2}".format(num1, num2, result))
    elif choice == "3":
        result = divide(num1, num2)
        print("\nTHE DIVISION OF {0} and {1} is {2}".format(num1, num2, result))
    elif choice == "1":
        result = mul(num1, num2)
        print("\nTHE PRODUCT OF {0} and {1} is {2}".format(num1, num2, result))
    else:
        print("!!!!!INVALID CHOICE!!!!!!")
    choice2 = input("DO YOU WISH TO CONTINUE[Y/N]:")








