def freq(Numbers, no):
    frequency = 0
    for i in Numbers:
        if i == no:
            frequency +=1
    return frequency

def main():
    n = int(input("Enter number of elements: "))
    numbers = []

    for i in range(n):
        num = int(input("Enter the number: "))
        numbers.append(num)

    search = int(input("Element to search: "))
    Ret = freq(numbers, search)
    print(f"Frequency of {search} is: {Ret}.")

if __name__ == "__main__":
    main()
    

