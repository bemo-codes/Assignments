import math
data = [5,7,9,11,13]
sum = 0
n=5
#Step 1: Calculate mean
for i in data:
    sum += i
mean = sum/n
print("Mean is: ", mean)
# Step 2: Calculate deviation from mean
deviation_mean = []
for i in data:
    d_mean = i - mean
    deviation_mean.append(d_mean)

#Step 3: Calculate square of the deviation
deviation_square=[]
for i in deviation_mean:
    sq = i**2
    deviation_square.append(sq)

#Step 4: Calculate variance
variance =[]
for i in deviation_square:
    variance_ = i/n
    variance.append(variance_)

#Step 5: Calculate standard deviation
standard_devi = []
for i in variance:
    sd = math.sqrt(i)
    standard_devi.append(sd)

for i,j,k in zip(data,variance, standard_devi):
    print(f"Variance of {i} is {j}")
    print(f"Standard deviation of {i} is {k}")


