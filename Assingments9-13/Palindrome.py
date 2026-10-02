def Palindrome(Number):
    num = 0
    while Number > 0:
        n = Number % 10
        num = num*10 + n
        Number = Number // 10
    return num

def main():
    No =int(input("Enter the number: "))

    Ret = Palindrome(No)

    if Ret == No:
        print("Number is Palindrome.")
    else:
        print("Number is not Palindrome.")

if __name__ == "__main__":
    main()