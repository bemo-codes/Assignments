def Length(Name):
    return len(Name)

def main():
    name = input("Enter Name: ")
    Ret = Length(name)

    print("Length of name is: ", Ret)

if __name__ == "__main__":
    main()