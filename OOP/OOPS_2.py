class Account:

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def create_account(self):
        print("Account successfully created for NAME:{} with BALANCE:{}!!!".format(self.name, self.balance))

    def withdraw(self, amount):
        if self.balance > 0:
            self.balance = self.balance - amount
        else:
            print("You don't have sufficient balance!!!")

    def deposit(self, balance):
        self.balance = self.balance + balance
        print("Deposit successful!!!")

    def check(self, name):
        print("Your current balance for ACCOUNT NAME:{} is:{}".format(name, self.balance))


if __name__ == '__main__':
    namelist = []
    while True:
        print("**********************ACCOUNT***************************")
        print("1.create account\n2.deposit\n3.withdraw\n4.check\n5.exit")
        print("**********************************************************")
        choice = int(input("Enter Your choice:"))
        print("**********************************************************")
        if choice == 1:
            holderName = input("Enter your name:")
            if holderName in namelist:
                print("already exists")
            else:
                namelist.append(holderName)
                account = Account(holderName)
                account.create_account()
        elif choice == 2:
            deposit = int(input("Enter the amount:"))
            account.deposit(deposit)
        elif choice == 3:
            withdraw_amount = int(input("Enter the Amount:"))
            account.withdraw(withdraw_amount)
        elif choice == 4:
            name1 = input("Enter your name:")
            account.check(name1)
        elif choice == 5:
            break
        else:
            print("Invalid choice")
