def ChkPrime(Number):
    factor = 0
    for i in range(1, Number+1):
        if Number % i ==0:
            factor += 1
    if factor == 2:
        return True
    else: 
        return False

# def main():
#     n = int(input("Enter number to be checked: "))
#     Ret = ChkPrime(n)
#     print(Ret)

# if __name__ == "__main__":
#     main()
        