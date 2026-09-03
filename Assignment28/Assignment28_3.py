import sys
def main():
    try:
        fobj = open(sys.argv[1], 'r')
        for line in fobj:
            print(line)

    except FileNotFoundError as fobj:
        print("File is not present in current directory.")

if __name__ == "__main__":
    main()