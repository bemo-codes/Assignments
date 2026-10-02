def Calci(No1, No2):

    print("Addition is:     ", No1 + No2)
    print("Substraction is:     ", No1 - No2)
    print("Multiplication is:     ", No1 * No2)
    print("Division is:     ", No1 / No2)

def main():
    No1 = int(input("Enter the first number: "))
    No2 = int(input("Enter the second number: "))

    Calci(No1, No2)
    
if __name__ == "__main__":
    main()