import sys
def main():
    div = lambda x: bool(x%5==0)
    no = int(sys.argv[1])
    print(div(no))

if __name__ == "__main__":
    main()