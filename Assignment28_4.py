import sys
def main():
    try:
        fobj = open(sys.argv[1], 'r')
        wobj = open(sys.argv[2], 'w')
        wobj.write(fobj.read())
            
    except FileNotFoundError as fobj:
        print("File is not present in current directory.")

if __name__ == "__main__":
    main()