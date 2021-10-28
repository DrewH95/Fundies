class BankAccount:


    def __init__(self, name, int_rate = 0.02, balance = 0): 
        self.name = name
        self.int_rate = int_rate
        self.balance = balance


    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < 0:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"{self.name}'s balance is ${self.balance}")
        return self

    def yield_interest(self):
        self.balance += (self.balance+self.int_rate)
        return self

chad = BankAccount("Chad")
chad.deposit(25).deposit(10).deposit(50).deposit(30).withdraw(150).display_account_info()


brad = BankAccount("Brad")
brad.deposit(25).deposit(10).deposit(50).deposit(40).withdraw(50).display_account_info()