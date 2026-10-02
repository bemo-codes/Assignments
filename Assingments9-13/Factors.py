def Factor(Number):
    factors = []
    for i in range(1, Number+1):
        if Number % i == 0:
            factors.append(i)
    return factors
      
def main():
    No = int(input("Enter the number: "))
    Ret = Factor(No)

    print(f"Factors are: {Ret}")

if __name__ == "__main__":
    main()