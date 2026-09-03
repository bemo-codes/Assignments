import sys

def main():
    try:
        fobj = open(sys.argv[1], "r")
        count = 0
        for line in fobj:
            words = line.split()
            count += len(words)
        print(f"Total words in file {sys.argv[1]} are {count}.")

    except FileNotFoundError as fobj:
        print("File is not present in current directory.")



if __name__ == "__main__":
    main()