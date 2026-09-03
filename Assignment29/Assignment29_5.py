import sys
import os

def Frequency(File, Word):
    fobj = open(File, "r")
    count = 0
    for line in fobj:
        words = line.lower().split()
        count += words.count(Word)
    print(f"Frequency of the {Word} is {count}.")
    fobj.close()

def main():
    Frequency(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()
