def Grade(marks):

    if marks >= 75:
        print("Distinction.")
    elif marks >= 60:
        print("First Class.")
    elif marks >= 50:
        print("Second Class.")
    elif marks < 50:
        print("Fail.")
    else:
        print("Invalid Marks.")

def main():
    Marks = int(input("Enter the Marks: "))
    Grade(Marks)

if __name__ == "__main__":
    main()
        
