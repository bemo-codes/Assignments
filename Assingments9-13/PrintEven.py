def Even(Number):
    for i in range(1,Number+1):
        if i % 2 == 0:
            print(i)


def main():
    print("Enter the number: ")
    No = int(input())

    print(f"All even number in range {No}: ")
    Even(No)

if __name__ == "__main__":
    main()
