import multiprocessing
import os
import time

def SumEven(Numbers):
    print("PID of SumEven is: ", os.getpid())
    print("Parent ID of SumEven is: ", os.getppid())
    sums = []
    for i in Numbers:
        sum = 0
        for j in range(1, i+1):
            if j % 2 == 0:
                sum += j
        sums.append(sum)
    return sums

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
    Result = pobj.map(SumEven, (nums,))

    print("Input numbers were: ")
    print(nums)
    print("Sum of even numbers: ")
    print(Result)

    end_time = time.perf_counter()
    print(f"Total time taken: {end_time-start_time} seconds.")

if __name__ == "__main__":
    main()



    