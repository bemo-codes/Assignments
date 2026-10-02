def ReverseNumber(Number):
    num = 0
    while Number > 0:
        n = Number % 10
        num = num*10 + n
        Number = Number // 10
    return num

def main():
    No = int(input("Enter the number: "))

    Ret = ReverseNumber(No)
    print(f"Reverse of the number is {Ret}.")

if __name__ == "__main__":
    main()
