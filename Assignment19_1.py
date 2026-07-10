def main():
    power = lambda x: x**2
    n = int(input("Enter Number: "))
    Ret = power(n)

    print(f"Square of {n} is: ", Ret)

if __name__ == "__main__":
    main()