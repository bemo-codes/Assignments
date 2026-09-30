def main():
    Strings = input("Enter numbers: ").split()
    five = list(filter(lambda x: len(x) > 5, Strings))

    print("Strings having length greater than 5: ", five)

if __name__ == "__main__":
    main()
