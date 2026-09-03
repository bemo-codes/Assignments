import os
import sys

def display(File):
    if os.path.exists(File):
        fobj = open(File,"r")
        data = fobj.read()
        print(data)

    else:
        print(f"{File} does not exist in directory.")

def main():
    display(sys.argv[1])

if __name__ == "__main__":
    main()