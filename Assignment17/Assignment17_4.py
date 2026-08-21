def fact(Number):
    sum = 0
    for i in range (1,Number):
        if Number % i == 0:
            sum +=i
    return sum

def main():
    n = int(input("Enter number: "))
    Ret = fact(n)
    print(f"Summation of factors of {n} is: ", Ret)

if __name__ == "__main__":
    main()