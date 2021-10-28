from Bank_Account import BankAccount


class User:


    def __init__(self, name, int_rate = 0.02, balance = 0):
        self.name = name
        self.int_rate = int_rate
        self.balance = balance

        def deposit(self, amount):
            self.deposit(amount)
            self.display_account_info
            return self

        def withdraw(self, amount):
            self.withdraw(amount)
            self.display_account_info
            return self
        
        def balance(self, amount):
            self.display_account_info(amount)
            return self

chad = BankAccount("Chad")
chad.deposit(25).deposit(1000).display_account_info()

brad = BankAccount("Brad")
brad.deposit(500).withdraw(100).display_account_info()