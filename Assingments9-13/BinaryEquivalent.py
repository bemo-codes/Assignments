# accept one number and print its binary equivalent
def BinaryEquivalent(Number):
    num = 0
    while Number > 0:
        num = num*10 + Number % 2
        Number = Number // 2

    print(num)

def main():
    No = int(input("Enter the number: "))
    BinaryEquivalent(No)
    
if __name__ == "__main__":
    main()
        
