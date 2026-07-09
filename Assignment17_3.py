def factorial(Number):
    fact = 1
    for i in range(1,Number+1):
        fact = fact * i

    return fact

def main():
    n = int(input("Enter number: "))
    Ret = factorial(n)
    print(f"Factorial of {n} is: ", Ret)

if __name__ == "__main__":
    main()