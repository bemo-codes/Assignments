def Cube(Number):
    return Number*Number*Number

def main():
    print("Enter the Number to be cubed: ")
    No = int(input())

    Ret = Cube(No)
    print(f"Cube of {No} is: ", Ret)

if __name__ == "__main__":
    main()