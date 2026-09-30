def main():
    numbers = [int(x) for x in input("Enter numbers: ").split()]
    Squares = list(map(lambda x: x**2, numbers))

    print(f"Squares of numbers: {Squares}")

if __name__ == "__main__":
    main()
