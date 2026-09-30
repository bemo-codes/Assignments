from functools import reduce
def main():
    Numbers = [int(x) for x in input("Enter numbers: ").split()]
    Multiplication = reduce(lambda x,y: x*y, Numbers)

    print("Multiplication of all elements is: ", Multiplication)

if __name__ == "__main__":
    main()
