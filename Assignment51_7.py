data = [6,7,8,9,10,11,12]
mean = 9
deviation = 2

for i in data:
    scaled_value = (i-mean)/deviation
    print(f"Scaled value of {i} is: {scaled_value}")
