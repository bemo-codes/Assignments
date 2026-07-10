import threading
def Sum(List):
    sum = 0
    for i in List:
        sum += i
    print("Sum of all elements is: ", sum)

def Product(List):
    mult = 1
    for i in List:
        mult *= i

    print("Product of all elements is: ", mult)

def main():
    nums = [int(x) for x in input("Enter numbers: ").split()]

    t1 = threading.Thread(target=Sum,args=(nums,))
    t1.start()
    t1.join()

    t2 = threading.Thread(target=Product, args=(nums,))
    t2.start()
    t2.join()

if __name__ == "__main__":
    main()
    