def main():
    Add = lambda x,y: x+y
    No1 = int(input("Enter the first number: "))
    No2 = int(input("Enter the second number: "))

    result = Add(No1, No2)
    print(f"Additon is: {result}")

if __name__ == "__main__":
    main()