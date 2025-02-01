print("NAME:- SANKET MAHAPATRA")
print("REGISTRATION NUMBER:- 2241013017")

class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be greater than 0.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance: {self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be greater than 0.")

    def get_balance(self):
        return f"Account balance: {self.balance}"

account1 = BankAccount("Sanket Mahapatra", 1000)

account1.deposit(500)
account1.withdraw(200)
print(account1.get_balance())
