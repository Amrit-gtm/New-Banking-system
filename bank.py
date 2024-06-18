class BankAccount:
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.balance

    def transfer(self, amount, other_account):
        if self.balance >= amount:
            self.balance -= amount
            other_account.deposit(amount)
            print(f"Transferred {amount} to {other_account.account_holder}. New balance is {self.balance}.")
        else:
            print("Insufficient funds for transfer.")

# Test cases
account1 = BankAccount("Alice")
account2 = BankAccount("Bob")

account1.deposit(100)
account1.withdraw(50)
print(account1.get_balance())  # Expected output: 50

account1.transfer(30, account2)
print(account1.get_balance())  # Expected output: 20
print(account2.get_balance())  # Expected output: 30

account1.withdraw(100)