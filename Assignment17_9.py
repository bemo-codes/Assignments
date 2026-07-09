def NoDigits(number):
    count = 0
    while number > 0:
        count += 1
        number = number // 10
    return count

def main():
    no = int(input("Enter number: "))
    Ret = NoDigits(no)
    print(f"Number of digits in {no} is: ", Ret)

if __name__ == "__main__":
    main()
        