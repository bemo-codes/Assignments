def Accept(List):
    min = List[0]
    for i in List:
        if i < min:
            min = i
    return min

def main():
    numbers = [int(x) for x in input("Enter numbers: ").split()]
    Ret = Accept(numbers)

    print("Minimum of numbers is: ", Ret)

if __name__ == "__main__":
    main()