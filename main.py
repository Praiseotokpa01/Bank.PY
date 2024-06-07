
class Account:
    def __init__(self, balance=0):
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            return True
        else:
            print("Insufficient funds!")
            return False

    def get_balance(self):
        return self._balance
