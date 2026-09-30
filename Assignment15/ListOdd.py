def main():
    Numbers = [int(x) for x in input("Enter numbers: ").split()]
    Odd = list(filter(lambda x: x % 2 != 0, Numbers))

    print("Odd numbers are: ", Odd)

if __name__ == "__main__":
    main()
