def Divisible(Number):
    if Number % 3 == 0 and Number % 5 == 0:
        print(f"{Number} is divisible by both 5 and 3.")
    elif Number % 3 == 0:
        print(f"{Number} is divisible by 3.")
    elif Number % 5 == 0:
        print(f"{Number} is divisible by 5.")
    else:
        print(f"{Number} is not divisible by both 3 and 5.")

def main():
    print("Enter the Number to be check for divisiblity(3&5): ")
    No = int(input())

    Divisible(No)

if __name__ == "__main__":
    main()
