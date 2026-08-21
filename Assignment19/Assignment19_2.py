def main():
    Multi = lambda x, y: x*y
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))

    Ret = Multi(n1,n2)
    print("Multiplication is: ", Ret)

if __name__ == "__main__":
    main()