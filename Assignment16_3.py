import sys

def Add(No1,No2):
    return No1 + No2

def main():
    no1 = int(sys.argv[1])
    no2 = int(sys.argv[2])
    Ret = Add(no1,no2)
    print("Addition is: ", Ret)

if __name__ == "__main__":
    main()

    