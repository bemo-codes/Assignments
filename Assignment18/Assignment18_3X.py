def Accept(List):
    min = List[0]
    for i in List:
        if i < min:
            min = i
    return min

def main():
    n = int(input("Enter number of elements: "))
    numbers = []

    for i in range(n):
        no = int(input("Enter the number: "))
        numbers.append(no)

    Ret = Accept(numbers)
    print("Minimum from the numbers is: ", Ret)

if __name__ == "__main__":
    main()
