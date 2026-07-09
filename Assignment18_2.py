def Accept(List):
    max = 0
    for i in List:
        if i > max:
            max = i
    return max

def main():
    numbers = [int(x) for x in input("Enter numbers: ").split()]
    Ret = Accept(numbers)

    print("Maximum of numbers is: ", Ret)

if __name__ == "__main__":
    main()