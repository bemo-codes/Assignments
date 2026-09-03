import multiprocessing

def SumSquare(List):
    squares = []
    for i in List:
       square = i*i
       squares.append(square)
    return squares

def main():
    data = [int(x) for x in input("Enter numbers: ").split()]

    pobj = multiprocessing.Pool()
    Result = pobj.map(SumSquare, (data,))

    pobj.close()
    pobj.join()
    print("Return is: ")
    print(Result)

if __name__ == "__main__":
    main()