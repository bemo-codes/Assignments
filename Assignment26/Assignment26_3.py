class Arithmetic:

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        print("Enter the first value: ")
        self.Value1 = int(input())
        print("Enter the second value: ")
        self.Value2 = int(input())

    def Addition(self):
       print("Addition is: " ,self.Value1 + self.Value2)
    
    def Substraction(self):
        print("Substraction is: ", self.Value1 - self.Value2)
    
    def Multiplication(self):
        print("Mutliplication is: ", self.Value1 * self.Value2)

    def Division(self):
        if self.Value2 == 0:
            print("Division by zero is not possible.")
        else:
            print("Division is: ", self.Value1 / self.Value2)

obj1 = Arithmetic()
obj2 = Arithmetic()
obj3 = Arithmetic()

obj1.Accept()
obj1.Addition()
obj1.Substraction()
obj1.Multiplication()
obj1.Division()
print("-"*40)
obj2.Accept()
obj2.Addition()
obj2.Substraction()
obj2.Multiplication()
obj2.Division()
obj1.Division()
print("-"*40)
obj3.Accept()
obj3.Addition()
obj3.Substraction()
obj3.Multiplication()
obj3.Division()