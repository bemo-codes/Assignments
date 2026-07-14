import multiprocessing
import os
import time

def Factorial(Numbers):
    print("PID of Factorial is: ", os.getpid())
    print("Parent ID of Factorial is: ", os.getppid())
    Facts = []
    for i in Numbers:
        fact = 1
        for j in range(1, i+1):
            fact *= j
        Facts.append(fact)
    return Facts

def main():
    print("Enter number of elements you want: ")

    n = int(input())
    nums=[]
    for i in range(1, n+1):
        print("Enter number: ")
        no = int(input())
        nums.append(no)

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()
    Result = pobj.map(Factorial, (nums,))

    print("Input numbers were: ")
    print(nums)
    print("Factorial of numbers: ")
    print(Result)

    end_time = time.perf_counter()
    print(f"Total time taken: {end_time-start_time} seconds.")

if __name__ == "__main__":
    main()



    