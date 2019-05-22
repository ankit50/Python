remainder = {}
while True:
    print("**********Birthday Remainder*************")
    print("1).Show BirthDay:\n2).Add BirthDay:\n3).Exit")
    choice = int(input("Enter The Choice(1-3):"))
    if choice == 1:
        if len(remainder.keys()) == 0:
            print("Noting To show!")
        else:
            name = input("Enter the name to look:")
            birthday = remainder.get(name, "NOt found")
            print(birthday)
    elif choice == 2:
        name = input("Enter friends Name:")
        date = input("Enter Birthdate:")
        remainder[name] = date
        print("Birthday Added Successfully")
    elif choice == 3:
        break
    else:
        print("Enter a Valid Choice")
