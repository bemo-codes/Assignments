def main():
    Odd = lambda x: bool(x % 2 != 0)
    No = int(input("Enter the number: "))

    result = Odd(No)
    print(f"Is {No} odd: {result}.")

if __name__ == "__main__":
    main()