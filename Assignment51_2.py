import math
data = 4,6,8,10,12
n = 5

mean = sum(data)/n
print(mean)

for i in data:
    variance =(i - mean)**2 / n 
    Deviation = math.sqrt(variance)
    print(f"Variance of {i} is: ", variance)
    print(f"Deviation of {i} is: {Deviation}")

