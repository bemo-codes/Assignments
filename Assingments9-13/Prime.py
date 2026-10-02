def Prime(Number):
    factor = 0
    for i in range(1, Number+1):
        if Number % i == 0:
            factor = factor + 1
    return factor
    

def main():
    print("Enter the number: ")
    No = int(input())

    Ret =Prime(No) 
    if Ret == 2:
        print(f"{No} is prime.")
    else: 
        print(f"{No} is not prime")
   

if __name__ == "__main__":
    main()