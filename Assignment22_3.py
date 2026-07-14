from MarvelleousNum import ChkPrime
import multiprocessing
import time
def prime(Numbers):
    count = 0
    primecount = []
    for i in Numbers:
        for j in range(1,i+1):
            if ChkPrime(j):
                count += 1
        primecount.append(count)
    return primecount

def main():
    nums = [int(x) for x in input("Enter numbers: ").split()]
    start_time = time.perf_counter()
    pobj = multiprocessing.Pool()
    Result = pobj.map(prime,(nums,))
    
    pobj.close()
    pobj.join()
    print(nums)

    print("Numbers are: ")
    print(nums)
    print("Prime numbers are:")
    print(Result)
    end_time = time.perf_counter()
    print(f"Total time taken: {end_time - start_time} seconds.")

if __name__ == "__main__":
    main()


# for i, j in zip(nums, Result):
#         print(f"Prime numbers between 1 to {i} are: {j}.")
       
