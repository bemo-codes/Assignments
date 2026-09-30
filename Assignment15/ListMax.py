from functools import reduce

def main():
    Numbers = [int(x) for x in input("Enter numbers: ").split()]
    Max = reduce(lambda x,y: max(x,y), Numbers)
    
    print("Maximum is: ", Max)

if __name__ == "__main__":
    main()
