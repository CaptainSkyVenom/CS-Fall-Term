class Account:

    accountcount = 0

    def __init__(self, pin, money):

        self.balance = money
        self.interestrate = 0
        self.pin = pin
        self.accountid = Account.accountcount
        Account.accountcount += 1
        self.isOpen = True

    def deposit(self, money, pin):
        if self.pin == pin:
            self.balance += money
            return 0
        else:
            print("Wrong Pin!")
            return 1

    def withdrawal(self, money, pin):
        if self.pin == pin:
            if self.balance >= money:
                self.balance -= money
                return money
            else:
                print("Your balance is: " + self.balance + ". You have insufficient funds. ")
                return 0
        else:
            print("Wrong Pin!")


    def transfer(self, acc2, money, pin):
        if self.pin == pin:
            if self.balance >= money:
                self.balance -= money
                acc2.balance += money
            else:
                print("Your balance is: " + self.balance + ". You have insufficient funds. ")
        else:
            print("Wrong Pin!")


    def close(self):
        if self.isOpen:
            self.isOpen = False
        else:
            print("Your bank account is already closed")




account1 = Account(1, 100)
account2 = Account(2, 200)

account1.deposit(10000, 1)
print(account1.balance)

account2.deposit(10000, 2)
print(account2.balance)

account2.deposit(10000, 1)
print(account2.balance)

account1.transfer(account2,5000,1)
print(account2.balance)
