def ChkGreater(No1, No2):

    if No1 > No2:
        print(f"{No1} is Greater than {No2}")
    elif No2 > No1:
        print(f"{No2} is Greater than {No1}")
    else:
        print("Both are equal")

def main():
    
    print("Enter first number: ")
    No1 = int(input())
    print("Enter second number: ")
    No2 = int(input())

    ChkGreater(No1,No2)

if __name__ == "__main__":
    main()
