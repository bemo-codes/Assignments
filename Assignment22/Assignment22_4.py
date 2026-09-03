import multiprocessing
import time
import os
def Pow5(Numbers):
    print(f"PID of process pow5 is: ", os.getpid())
    add =[]
    for i in Numbers:
        sum = 0
        for j in range(0, i+1):
            sum = sum + j**5
        add.append(sum)
    return add
    

def main():
    print("How many numbers do you want to enter: ")
    n = int(input())

    numbers = []
    for i in range(1, n+1):
        print("Enter the number: ")
        num = int(input())
        numbers.append(num)

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()
    
    result = pobj.map(Pow5,(numbers,))
    print("-"*40)
    print("Input numbers are: ")
    print(numbers)
    print("Addition of power of  5 of those numbers are: ")
    print(result)
    end_time = time.perf_counter()

    print(f"Total time taken is: {end_time-start_time} seconds")

if __name__ == "__main__":
    main()