import sys

def Check(Number):
    if Number == 0:
        print("Zero.")
    elif Number > 0:
        print("Positive number.")
    else:
        print("Negative number.")

def main():
    no = int(sys.argv[1])
    Check(no)

if __name__ == "__main__":
    main()