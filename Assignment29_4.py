import sys
import os

def Compare(File1, File2):
    fobj1 = open(File1, "r")
    fobj2 = open(File2, "r")

    while True:
        if fobj1.read() == fobj2.read():
            print("Success")
            break
        else:
            print("Failure")

    fobj1.close()
    fobj2.close()

def main():
    Compare(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()        
    