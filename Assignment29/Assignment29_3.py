import os
import sys

def Copy(File):
    if os.path.exists(File):
        fobj = open(File,"r")
        wobj = open("Demoo.txt", "w")
        wobj.write(fobj.read())
    else:
        print(f"{File} does not exist in directory.")
def main():
    Copy(sys.argv[1])
if __name__ == "__main__":
    main()