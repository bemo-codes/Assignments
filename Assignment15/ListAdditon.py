from functools import reduce

def main():
    Numbers = [int(x) for x in input("Enter numbers: ").split()]
    Add = reduce(lambda x,y: x+y, Numbers)
    
    print("Addition of numbers is: ", Add)

if __name__ == "__main__":
    main()
