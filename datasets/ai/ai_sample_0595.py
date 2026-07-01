class BankAccount:
    def __init__(self):
        self._balance = 0

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Amount must be greater than 0")

        self._balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Amount must be greater than 0")
        if amount > self._balance:
            raise ValueError("Insufficient funds")

        self._balance -= amount