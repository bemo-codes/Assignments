import sys

def main():
    fobj = open(sys.argv[1], "r")
    for line in fobj:
        if sys.argv[2] in line:
            print(f"{sys.argv[2]} is present in the file.")
            break
        else:
            print(f"{sys.argv[2]} is not present.")
if __name__ == "__main__":
    main()