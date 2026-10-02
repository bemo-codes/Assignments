def PerfectNumber(Number):
    sum = 0
    for i in range(1, Number):
        if Number % i == 0:
            sum += i
    print(sum)
        
    if sum == Number:
        print(f"{Number} is a perfect Number.")
    else:
        print(f"{Number} is not perfect number.")

def main():
    No = int(input("Enter the number: "))
    PerfectNumber(No)

if __name__ == "__main__":
    main()