import multiprocessing
import os
import time
def factorial(Numbers):
    print("PID of factorial is: ", os.getpid())
    fact = []

    for i in Numbers:
        mult = 1
        for j in range(1,i+1):
            mult = mult * j
        fact.append(mult)
    return fact

def main():
    st_time = time.perf_counter()
    nums = [int(x) for x in input("Enter numbers: ").split()]

    pobj = multiprocessing.Pool()
    Result = pobj.map(factorial, (nums,))

    pobj.close()
    pobj.join()
    print("Numbers are: ")
    print(nums)
    print("Result is: ")
    print(Result)
    end_time = time.perf_counter()
    print(f"Total time taken: {end_time-st_time:.4f} seconds.")
if __name__ == "__main__":
    main()
            