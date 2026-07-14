import multiprocessing
import os
import time

def CountEven(Numbers):
    print("PID of CountEven is: ", os.getpid())
    print("Parent ID of CountEven is: ", os.getppid())
    Counts = []
    for i in Numbers:
        count = 0
        for j in range(1, i+1):
            if j % 2 == 0:
                count += 1
        Counts.append(count)
    return Counts

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
    Result = pobj.map(CountEven, (nums,))

    print("Input numbers were: ")
    print(nums)
    print("Count of even numbers is: ")
    print(Result)

    end_time = time.perf_counter()
    print(f"Total time taken: {end_time-start_time} seconds.")

if __name__ == "__main__":
    main()



    