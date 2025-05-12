class Account:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid or insufficient funds")

    def get_balance(self):
        return self.__balance


acc = Account()
acc.deposit(1000)
acc.withdraw(300)
print("Remaining balance:", acc.get_balance())
