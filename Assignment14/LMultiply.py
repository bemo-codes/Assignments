def main():
    Multiply = lambda x,y: x*y
    No1 = int(input("Enter the first number: "))
    No2 = int(input("Enter the second number: "))

    result = Multiply(No1,No2)
    print(f"Multiplication is: {result}")

if __name__ == "__main__":
    main()