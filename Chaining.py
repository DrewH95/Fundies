class User:
    def __init__(self):
        self.accountBalance = 100

    def makeDeposit(self, amount):
        self.accountBalance += amount
        return self
    def makeWithdrawal(self, amount):
        self.accountBalance -= amount
        return self
    def checkBalance (self):
        print(f"{self.name}'s' Balance is ${self.accountBalance}")
        return self
        
Chad = User()
Chad.name = "Chad"
Chad.accountBalance = 100

Chad.makeDeposit(25).makeDeposit(10).makeDeposit(50).makeDeposit(30).makeWithdrawal(15).checkBalance()

Brad = User()
Brad.name = "Brad"
Brad.accountBalance = 200

Brad.makeDeposit(25).makeDeposit(10).makeDeposit(50).makeDeposit(40).makeWithdrawal(25).checkBalance()

Dad = User()
Dad.name = "Dad"
Dad.accountBalance = 100000

Dad.makeDeposit(1000).makeDeposit(1000).makeDeposit(5000).makeDeposit(5000).makeWithdrawal(1).checkBalance()