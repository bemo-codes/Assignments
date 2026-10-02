def CountDigit(Number):
    count = 0
    while Number > 0:
        count += 1
        Number = Number // 10
    return count

def main():
    print("Enter the number: ")
    No = int(input())

    Ret = CountDigit(No)
    print("Number of digits in the number: ", Ret)

if __name__ == "__main__":
    main()
    