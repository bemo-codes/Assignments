import threading

def EvenFactor(number):
    sum = 0
    for i in range(1,number):
        if number % i == 0:
            if i % 2 ==0:
                sum += i
    print("Additon of even factors is: ", sum)

def OddFactor(number):
    sum = 0
    for i in range(1,number):
        if number % i == 0:
            if i % 2 != 0:
                sum += i
    print("Addition of odd factors is: ", sum)

def main():
    n = int(input("Enter the number: "))

    t1 = threading.Thread(target=EvenFactor, args=(n,))
    t2 = threading.Thread(target=OddFactor, args= (n,))

    t1.start()
    t2.start()

if __name__ == "__main__":
    main()