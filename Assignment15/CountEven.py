def main():
    numbers = [int(x) for x in input("Enter numbers: ").split()]
    Even = list(filter(lambda x: x%2==0, numbers))

    print("Number of even numbers: ", len(Even))

if __name__ == "__main__":
    main()
