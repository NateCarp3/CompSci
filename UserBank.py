

class BankAccount:
    bank_name = "Nate's Bank"

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount    # the specific user's account increases by the amount of the value received
        return self
    def withdrawal(self, amount):
        self.balance -= amount    # the specific user's account increases by the amount of the value received
        return self
    def yield_interest(self):
        self.balance *= (self.int_rate + 1) # the specific user's account is multiplied by 1 + interest rate
        return self
    def display_info(self): # the specific user's balance
        print (self.balance)
        return self


Account1 = BankAccount(0.4, 0)
Account2 = BankAccount(0.3, 0)

Account1.deposit(100).deposit(90).deposit(10).withdrawal(20).yield_interest().display_info()
Account2.deposit(90).deposit(210).withdrawal(20).withdrawal(15).withdrawal(35).withdrawal(30).yield_interest().display_info()


    





