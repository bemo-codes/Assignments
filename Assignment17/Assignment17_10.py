def SumDigits(Number):
    sum = 0
    while Number > 0:
        sum += Number % 10
        Number = Number // 10
    
    return sum

def main():
    n = int(input("Enter number: "))
    Ret = SumDigits(n)

    print(f"Addition of numbers is: ", Ret)

if __name__ == "__main__":
    main()