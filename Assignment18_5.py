from MarvelleousNum import ChkPrime
def ListPrime(Numbers):
    prime = []
    for i in Numbers:
        if ChkPrime(i) == True:
            prime.append(i)

    sumP = 0
    for i in prime:
        sumP += i
    return sumP

def main():
    numbers = []
    n = int(input("Enter number of elements: "))
    for i in range(n):
        num = int(input("Enter number: "))
        numbers.append(num)

    Ret = ListPrime(numbers)
    print("Addition of all prime numbers is: ", Ret)

if __name__ == "__main__":
    main()
