def Nsum(Number):
    sum = 0
    for i in range(0,Number+1):
        sum = sum + i
    return sum

def main():
    print("Enter the number: ")
    No = int(input())

    Ret = Nsum(No)

    print(f"Sum of {No} natural numbers is: ", Ret)

if __name__ == "__main__":
    main()