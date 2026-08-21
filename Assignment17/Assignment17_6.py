def pattern(Number):
    for i in range(Number,0,-1):
        print("* " * i)
                      
def main():
    n = int(input("Enter number: "))
    pattern(n)

if __name__ == "__main__":
    main()