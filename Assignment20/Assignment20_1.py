import threading

def DisplayEven():

    for i in range(2,21,2):
        print(i, end = " ")
    print(" ")

def DisplayOdd():
    for i in range(1, 20, 2):
        print(i, end = " ")

def main():

    t1 = threading.Thread(target= DisplayEven)
    t2 = threading.Thread(target=DisplayOdd)

    print("Even numbers are: ")
    t1.start()
    print("Odd numbers are: ")
    t2.start()

if __name__ == "__main__":
    main()