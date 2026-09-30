def main():
    Max = lambda x, y, z: max(x, y, z)

    No1 = int(input("Enter the first number: "))
    No2 = int(input("Enter the second number: "))
    No3 = int(input("Enter the third number: "))

    result = Max(No1, No2, No3)
    print(f"Maximum of three numbers is: {result}.")

if __name__ == "__main__":
    main()