print("NAME:- SANKET MAHAPATRA")
print("REGISTRATION NUMBER:- 2241013017")

class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance
        
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. Current balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. Current balance: {self.__balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")
    
    def display_balance(self):
        print(f"Current balance: {self.__balance}")
    
    def get_balance(self):
        return self.__balance

print("In this program, the balance attribute is private (using __balance), which means it cannot be accessed directly from outside the class. This ensures the balance is protected from accidental changes.\n")
print("The deposit method adds money to the account balance, and the withdraw method subtracts from the balance if there are sufficient funds. These methods control how the balance can be modified.\n")
print("By making the balance private, we prevent unauthorized or accidental modifications from outside the class, thus improving data security and integrity.\n")
print("Private attributes and methods ensure that the data is accessed and modified only in a controlled way, which helps maintain the correctness of the class behavior.\n")

account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
account.display_balance()
