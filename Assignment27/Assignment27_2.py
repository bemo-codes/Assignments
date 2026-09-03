class BankAccount:
    ROI = 10.5

    def __init__(self):
        name = input("Enter name: ")
        balance = int(input("Enter Balance Amount: "))
        self.name = name
        self.balance = balance

    def Display(self):
        print("Name is: ",self.name)
        print("Balance is: ", self.balance)
    
    def Deposit(self):
        amt = int(input("Enter Amount to be deposited: "))
        self.balance += amt
        print(f"Balance after deposit: {self.balance}")

    def Withdraw(self):
        amt = int(input("Enter Amount to be deducted: "))
        self.balance -= amt
        print(f"Balance after deduction: {self.balance}")

    def CalculateInterest(self):
        Interest = (self.balance * BankAccount.ROI) / 100
        print("Rate of interest is: ", Interest)

obj1 = BankAccount()
obj1.Display()
obj1.Deposit()
obj1.Withdraw()
obj1.CalculateInterest()

obj2 = BankAccount()
obj2.Display()
obj2.Deposit()
obj2.Withdraw()
obj2.CalculateInterest()

obj3 = BankAccount()
obj3.Display()
obj3.Deposit()
obj3.Withdraw()
obj3.CalculateInterest()
