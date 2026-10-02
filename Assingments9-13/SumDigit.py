def SumDigit(Number):
    sum = 0
    while Number > 0:
        sum = sum + Number % 10
        Number = Number // 10

    return sum

def main():
    print("Enter a number: ")
    No = int(input())

    Ret = SumDigit(No)
    print("Sum of digits is: ", Ret)

if __name__ == "__main__":
    main()

