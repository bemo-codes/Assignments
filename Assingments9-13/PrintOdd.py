def Odd(Number):
    for i in range(1,Number+1):
        if i % 2 != 0:
            print(i)


def main():
    print("Enter the number: ")
    No = int(input())

    print(f"All Odd number in range of {No}: ")
    Odd(No)

if __name__ == "__main__":
    main()
