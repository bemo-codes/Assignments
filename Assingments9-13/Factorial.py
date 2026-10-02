def Factorial(Number):
    mul = 1
    for i in range(1, Number+1):
        mul = mul * i
    
    return mul

def main():
    print("Enter the number: ")
    No = int(input())

    Ret = Factorial(No)
    print(f"Factorial of {No} is: ", Ret)

if __name__ == "__main__":
    main()

