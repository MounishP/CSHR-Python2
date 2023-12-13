"""
Create a base class Account with attributes account_number and balance.
Derive a class SavingsAccount from Account with an additional attribute interest_rate.
Implement methods to display the account balance and calculate interest for the savings account.
"""


class Account:
    def __init__(self, accountNumber, balance):
        self.accountNumber = accountNumber
        self.balance = balance

    def display(self):
        print(f"Account Number: {self.accountNumber} as Balance: {self.balance}")


class SavingAccount(Account):
    def __init__(self, accountNumber, balance, roi):
        super().__init__(accountNumber, balance)
        self.roi = roi

    def cal_interest(self):
        return self.balance * self.roi / 100


mounish = SavingAccount(123456789,200000,7.25)
mounish.display()
print(mounish.cal_interest())
