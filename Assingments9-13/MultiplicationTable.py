def Table(Number):
    for i in range(1,11):
        n = i * Number
        print(n)

def main():
    print("Enter the number for Multiplication table: ")
    No = int(input())
    print("-"*20)
    print("Table is: ")
    Table(No)

if __name__ == "__main__":
    main()
    