class User:
    def __init__(self):
        self.accountBalance = 100

    def makeDeposite(self, amount):
        self.accountBalance += amount
    def makeWithdrawal(self, amount):
        self.accountBalance -= amount
    def checkBalance (self):
        print(f"{self.name}'s Balance is ${self.accountBalance}")
Chad = User()
Chad.name = "Chad"
Chad.accountBalance = 100

Chad.makeDeposite(25)
Chad.makeDeposite(10)
Chad.makeDeposite(50)
Chad.makeDeposite(30)
Chad.makeWithdrawal(15)
Chad.checkBalance()

Brad = User()
Brad.name = "Brad"
Brad.accountBalance = 200

Brad.makeDeposite(25)
Brad.makeDeposite(10)
Brad.makeDeposite(50)
Brad.makeDeposite(40)
Brad.makeWithdrawal(25)
Brad.checkBalance()

Dad = User()
Dad.name = "Dad"
Dad.accountBalance = 100000

Dad.makeDeposite(1000)
Dad.makeDeposite(1000)
Dad.makeDeposite(5000)
Dad.makeDeposite(5000)
Dad.makeWithdrawal(1)
Dad.checkBalance()
