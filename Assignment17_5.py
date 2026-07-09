def prime(number):
    factors = 0
    for i in range(1,number+1):
        if number % i == 0:
            factors +=1
    
    if factors == 2:
        print("Number is prime.")
    else:
        print("Number is not prime.")

def main():
    n = int(input("Enter the number: "))
    prime(n)

if __name__ == "__main__":
    main()
    