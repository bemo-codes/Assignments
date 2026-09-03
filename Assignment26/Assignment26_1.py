class Demo:
    Value = 10                         #class varialbles
    def __init__(self, no1, no2):
        self.no1 = no1                 #instance variables  
        self.no2 = no2

    def fun(self):                     #instance method
        print(self.no1)
        print(self.no2)

    def gun(self):
        print(self.no1)
        print(self.no2)
        
obj1 = Demo(21, 11)                    #object creation this passes value in constructor i.e. into __init__ method
obj2 = Demo(51,101) 

obj1.fun()
obj2.fun()
obj1.gun()
obj2.gun()
