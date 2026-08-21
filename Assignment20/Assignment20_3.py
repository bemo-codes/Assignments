import threading

def EvenList(numbers):
    sum = 0
    for i in numbers:
        if i % 2 == 0:
            sum += i
    print("Sum of Even numbers is: ", sum)

def OddList(numbers):
    sum = 0
    for i in numbers:
        if i % 2 != 0:
            sum += i
    print("Sum of Odd numbers is: ", sum)

def main():
    Nums = [int(x) for x in input("Enter numbers: ").split()]

    t1 = threading.Thread(target=EvenList, args=(Nums,))
    t2 = threading.Thread(target=OddList, args=(Nums,))

    t1.start()
    t2.start()

if __name__ == "__main__":
    main()