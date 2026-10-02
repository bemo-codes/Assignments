def Square(Number):
    return Number*Number

def main():
    print("Enter number to be squared : ")
    No = int(input())

    Ret = Square(No)
    print("Square of number is: ", Ret)

if __name__ == "__main__":
    main()