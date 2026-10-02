def Rectangle(Length, Width):
    Area = Length * Width
    return Area

def main():
    L = int(input("Enter length of rectangle: "))
    W = int(input("Enter width of rectangle: "))
    Ret = Rectangle(L,W)

    print("Area of Rectangle is: ", Ret)

if __name__ == "__main__":
    main()

