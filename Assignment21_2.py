import threading
def Max(Numbers):
    max = 0
    for i in Numbers:
        if i > max:
            max = i
    print("Maximum element is: ", max)

def Min(Numbers):
    min = 0
    for i in Numbers:
        if i < min:
            min = i
    print("Minimum element is: ", min)

def main():
    nums = [int(x) for x in input("Enter numbers: ").split()]

    t1 = threading.Thread(target=Max, args=(nums,))
    t1.start()
    t1.join()

    t2 = threading.Thread(target=Min, args=(nums,))
    t2.start()
    t2.join()

if __name__ == "__main__":
    main()