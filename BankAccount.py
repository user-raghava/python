class BankAccount:
    def __init__(self, account_holder, ifsc, balance=0):
        self.account_holder = account_holder
        self.ifsc = ifsc
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Insufficient balance.")

# Creating an object of BankAccount
account1 = BankAccount("Rahul", "IFSC001", 5000)

# Calling methods using the object
account1.deposit(1500)
account1.withdraw(2000)