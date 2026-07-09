def pattern(number):

    for i in range(1, number + 1):
        print(" ")
        for j in range(1, i+1):
            print(j, end = ' ')

def main():
    n = int(input("Enter number: "))
    pattern(n)

if __name__ == "__main__":
    main()
