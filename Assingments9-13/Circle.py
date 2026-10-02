def Circle(radius):
    Area = 3.14 * radius * radius
    return Area

def main():
    r = int(input("Enter radius of circle: "))
    Ret = Circle(r)
    print("Area of circle: ", Ret)

if __name__ == "__main__":
    main()