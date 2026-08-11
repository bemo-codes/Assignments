import sys

def main():
    try:
        fobj = open(sys.argv[1],'r')
        data = True                         #Created a bool to run loop
        count = 0
        while data:
            data = fobj.readline()
            count += 1
        print(count)

    except FileNotFoundError as fobj:
        print("File is not present in current directory.")


if __name__ =="__main__":
    main()