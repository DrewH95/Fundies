class User:
    def __init__(self):
        self.accountBalance = 100

    def makeDeposit(self, amount):
        self.accountBalance += amount
    def makeWithdrawal(self, amount):
        self.accountBalance -= amount
    def checkBalance (self):
        print(f"{self.name}'s Balance is ${self.accountBalance}")
Chad = User()
Chad.name = "Chad"
Chad.accountBalance = 100

Chad.makeDeposit(25)
Chad.makeDeposit(10)
Chad.makeDeposit(50)
Chad.makeDeposit(30)
Chad.makeWithdrawal(15)
Chad.checkBalance()

Brad = User()
Brad.name = "Brad"
Brad.accountBalance = 200

Brad.makeDeposit(25)
Brad.makeDeposit(10)
Brad.makeDeposit(50)
Brad.makeDeposit(40)
Brad.makeWithdrawal(25)
Brad.checkBalance()

Dad = User()
Dad.name = "Dad"
Dad.accountBalance = 100000

Dad.makeDeposit(1000)
Dad.makeDeposit(1000)
Dad.makeDeposit(5000)
Dad.makeDeposit(5000)
Dad.makeWithdrawal(1)
Dad.checkBalance()
