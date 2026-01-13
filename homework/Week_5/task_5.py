class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.__owner = owner
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposit {amount} successfully made.")
        else:
            print("Error: Deposit amount must be positive!")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn {amount}. Remaining balance: {self.__balance}")
        else:
            print("Error: Insufficient funds!")

    def get_balance(self):
        return self.__balance

account = BankAccount("Artem", 1000)

print(f"Balance: {account.get_balance()}")

account.deposit(500)
account.deposit(-100)

account.withdraw(200)
account.withdraw(5000)