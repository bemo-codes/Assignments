def Accept(List):
    sum = 0
    for i in List:
        sum += i
    return sum

def main():
    numbers = [int(x) for x in input("Enter numbers: ").split()]
    Ret = Accept(numbers)

    print("Addition of numbers is: ", Ret)

if __name__ == "__main__":
    main()