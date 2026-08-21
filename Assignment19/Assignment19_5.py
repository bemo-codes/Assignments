from functools import reduce
from MarvelleousNum import ChkPrime
def main():
    numbers = [int(x) for x in input("Enter the numbers: ").split()]
    filt = list(filter(lambda x: bool(ChkPrime(x)), numbers))
    ten = list(map(lambda x: x*2, filt))
    product = reduce(lambda x, y: max(x,y), ten)

    print(f"List after filter: ", filt)
    print("List after map: ", ten)
    print("Result of reduce: ", product)

if __name__ == "__main__":
    main()
