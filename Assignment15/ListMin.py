from functools import reduce

def main():
    Numbers = [int(x) for x in input("Enter numbers: ").split()]
    Min = reduce(lambda x,y: min(x,y), Numbers)
    
    print("Minimum is: ", Min)

if __name__ == "__main__":
    main()
