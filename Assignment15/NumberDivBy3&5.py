def main():
    Numbers = [int(x) for x in input("Enter numbers: ").split()]
    Div = list(filter(lambda x: x % 3 ==0 and x % 5 == 0, Numbers))

    print("Number divisible by 3 & 5 both are: ", Div)

if __name__ == "__main__":
    main()
