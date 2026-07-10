import threading
from MarvelleousNum import ChkPrime
def Prime(Numbers):

    for i in Numbers: 
        if ChkPrime(i):
            print(i, end=" ")
    print(" ")

def NonPrime(Numbers):

    for i in Numbers:
        if not ChkPrime(i):
            print(i, end=" ")
    
def main():
    nums = [int(x) for x in input("Enter Numbers: ").split()]
    print("Prime numbers are: ")
    t1 = threading.Thread(target=Prime, args=(nums,))
    t1.start()
    t1.join()

    print("Non prime numbers are: ")
    t2 = threading.Thread(target=NonPrime, args=(nums,))
    t2.start()
    t2.join()

if __name__ == "__main__":
    main()