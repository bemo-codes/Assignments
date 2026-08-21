from functools import reduce
def main():
    numbers = [int(x) for x in input("Enter the numbers: ").split()]
    filt = list(filter(lambda x: 70 <= x <= 90, numbers))
    ten = list(map(lambda x: x + 10, filt))
    product = reduce(lambda x, y: x*y, ten)

    print(f"List after filter: ", filt)
    print("List after map: ", ten)
    print("Result after reduce: ", product)

if __name__ == "__main__":
    main()