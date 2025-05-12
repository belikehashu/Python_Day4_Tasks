class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, balance):
        self.accounts[name] = balance

    def deposit(self, name, amount):
        if name in self.accounts:
            self.accounts[name] += amount

    def withdraw(self, name, amount):
        if name in self.accounts and self.accounts[name] >= amount:
            self.accounts[name] -= amount
        else:
            print("Insufficient balamce or account not found")

    def check_balance(self, name):
        return self.accounts.get(name, "Account not found")


b = Bank()
b.create_account("Ali", 1000)
b.deposit("Ali", 500)
b.withdraw("Ali", 300)
print("Balance:", b.check_balance("Ali"))
