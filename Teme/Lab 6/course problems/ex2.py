# 2 ------------------------------------------------
# Design a bank account system with a base class Account and subclasses SavingsAccount and CheckingAccount.
# Implement methods for deposit, withdrawal, and interest calculation.

class Account:
    def __init__(self, id, name, balance):
        self.name = name
        self.balance = balance
        self.id = id

    def deposit(self, amount):
        self.balance += amount

    def withdrawal(self, amount):
        self.balance -= amount

class SavingsAccount(Account):
    def __init__(self, id, name, balance, years, annual_interest_rate = 0.04):
        super().__init__(id, name, balance)
        self.annual_interest_rate = annual_interest_rate
        self.years = years

    def interest_calculation(self):
        return self.balance * self.annual_interest_rate * self.years

class CheckingAccount(Account):
    def __init__(self, id, name, min_balance, annual_interest_rate = 0.008):
        super().__init__(id, name, min_balance)
        self.annual_interest_rate = annual_interest_rate

    def interest_calculation(self):
        return self.balance * self.annual_interest_rate

sa = SavingsAccount(0, "Mihai Ungureanu", 23500, 2)
ca = CheckingAccount(1, "Elena Boaghe", 48100)

print(sa.interest_calculation())
sa.withdrawal(12000)
print(sa.interest_calculation())
print(ca.interest_calculation())