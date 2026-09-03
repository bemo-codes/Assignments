class Circle:
    PI = 3.14
    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        print("Enter the Radius of circle: ")
        rad = int(input())
        self.Radius = rad
        return self.Radius

    def CalculateArea(self):
        area = Circle.PI * self.Radius * self.Radius
        self.Area = area
        return self.Area
    
    def CalculateCircumference(self):
        circumference = 2 * Circle.PI * self.Radius
        self.Circumference = circumference
        return self.Circumference

    def Display(self):
        print(f"Radius is: {self.Radius}")
        print(f"Area of circle is: {self.Area}")
        print(f"Circumference of circle is: {self.Circumference:.4f}")

obj1 = Circle()
obj2 = Circle()

obj1.Accept()
obj1.CalculateArea()
obj1.CalculateCircumference()
obj1.Display()

obj2.Accept()
obj2.CalculateArea()
obj2.CalculateCircumference()
obj2.Display()
    
