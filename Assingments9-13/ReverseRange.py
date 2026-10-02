def ReverseRange(Number):

    for i in range(Number, 0, -1):
        print(i)

def main():
    No = int(input("Enter the number: "))
    ReverseRange(No)

if __name__ == "__main__":
    main()