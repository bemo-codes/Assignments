def Star(Number):
    for i in range(0, Number):
        print("*", end = " ")

def main():
    no = int(input("Enter number of stars: "))
    Star(no)

if __name__ == "__main__":
    main()
