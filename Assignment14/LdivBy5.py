def main():
    Div = lambda x: bool(x % 5 == 0)
    No = int(input("Enter the number: "))

    result = Div(No)
    print(f"Is {No} divisible by 5: {result}.")

if __name__ == "__main__":
    main()