print("NAME:- SANKET MAHAPATRA")
print("REGISTRATION NUMBER:- 2241013017\n")

class InsufficientFundsError(Exception):
    def __init__(self, balance, withdrawal_amount):
        super().__init__(f"Insufficient funds! Balance: {balance}, Withdrawal Attempt: {withdrawal_amount}")
        self.balance = balance
        self.withdrawal_amount = withdrawal_amount

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return self.balance

try:
    account = BankAccount(1000)
    print(f"Initial Balance: {account.balance}")
    account.withdraw(1500)
except InsufficientFundsError as e:
    print(f"Error: {e}")

print("\nExplanation: This program defines a custom exception class InsufficientFundsError that displays the balance and withdrawal amount when an error occurs.\n")
print("Explanation: The withdraw() method in the BankAccount class checks if the withdrawal amount exceeds the balance and raises an exception if funds are insufficient.\n")
print("Explanation: When the exception is raised, it provides a meaningful error message with details of the balance and attempted withdrawal.\n")
print("Explanation: Custom exceptions improve error handling by providing specific and clear error messages, making debugging and problem resolution easier.\n")
