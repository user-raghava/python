class BankAccount:
    def __init__(self, account_holder, ifsc, balance=0):
        self.account_holder = account_holder
        self.ifsc = ifsc
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.account_holder} deposited {amount}. New balance is {self.balance}.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.account_holder} withdrew {amount}. New balance is {self.balance}.")
        else:
            print(f"{self.account_holder} has insufficient balance.")

    def transfer(self, other_account, amount):
        if amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount
            print(f"{self.account_holder} transferred {amount} to {other_account.account_holder}.")
            print(f"{self.account_holder}'s new balance: {self.balance}")
            print(f"{other_account.account_holder}'s new balance: {other_account.balance}")
        else:
            print(f"Transfer failed. {self.account_holder} has insufficient balance.")

# Creating two objects of BankAccount
account1 = BankAccount("Rahul", "IFSC001", 5000)
account2 = BankAccount("Amit", "IFSC002", 3000)

# Testing methods
account1.deposit(1500)
account1.withdraw(2000)
account1.transfer(account2, 2500)
