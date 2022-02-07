class Account:
    def __init__(self, owner, balance=100):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Account owner: {self.owner} \nAccount owner: {self.balance}"

    def deposit (self, amount):
        self.balance += amount
        print(f"Deposit accepted! New balance: {self.balance}")

    def withdraw (self, amount):
        if self.balance - amount < 0:
            print("Funds Unavailable! Balance less than 0")
        else:
            self.balance -= amount
            print(f"Withdrawal accepted! New balance: {self.balance}")

acct1 = Account('Jose',100)
print(acct1)
print(acct1.owner)
print(acct1.balance)
acct1.deposit(50)
acct1.withdraw(50)
acct1.withdraw(500)

