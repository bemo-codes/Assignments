import os
import sys
def check(File):
    Ret = os.path.exists(File)
    if Ret == True:
        print(f"{File} file exists in directory.")
    else:
        print(f"{File} does not exist in directory.")

def main():
    check(sys.argv[1])

if __name__ == "__main__":
    main()