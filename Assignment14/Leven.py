def main():
    Even = lambda x: bool(x % 2 == 0)
    No = int(input("Enter the number: "))

    result = Even(No)
    print(f"Is {No} even: {result}.")

if __name__ == "__main__":
    main()