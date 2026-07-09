import sys

def ChkNum(Number):
    if Number % 2 == 0:
        print("Even number.")
    else:
        print("Odd number.")

def main():
    no = int(sys.argv[1])
    ChkNum(no)

if __name__ == "__main__":
    main()