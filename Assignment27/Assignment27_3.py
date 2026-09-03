class Numbers:

    def __init__(self):
        value = int(input("Enter Value: "))
        self.Value = value

    def ChkPrime(self):
        factor = 0
        for i in range(1, self.Value+1):
            if self.Value % i ==0:
                factor += 1
        if factor == 2:
            print(f"Is number prime: " ,True)
        else: 
            print(f"Is number prime: " ,False)
        
    def PerfectNumber(self):
        sum = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                sum += i
            
        if sum == self.Value:
            print("Is number perfect number: " ,True)
        else:
            print("Is number perfect number: " ,False)
        
    def Factor(self):
        factors = []
        for i in range(1, self.Value+1):
            if self.Value % i == 0:
                factors.append(i)
        print(f"Factors are: " ,factors)

    def SumFactor(self):
        sum = 0
        for i in range(1, self.Value+1):
            if self.Value % i == 0:
                sum += i
        print("Sum of factors is: ", sum)

obj1 = Numbers()
obj1.ChkPrime()
obj1.PerfectNumber()
obj1.Factor()
obj1.SumFactor()

obj2 = Numbers()
obj2.ChkPrime()
obj2.PerfectNumber()
obj2.Factor()
obj2.SumFactor()

obj3 = Numbers()
obj3.ChkPrime()
obj3.PerfectNumber()
obj3.Factor()
obj3.SumFactor()