import matplotlib.pyplot as plt
import numpy as np

def main():
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    n = len(X)

    sum = 0
    for i in X:
        sum +=i
    print("Sum is: ", sum)
    mean_x = sum/n
    print("Mean of X is: ", mean_x)

    for i in Y:
        sum +=i
    print("Sum is: ", sum)
    mean_y = sum/n
    print("Mean of Y is: ", mean_y)

    numerator = 0
    denominator = 0

    for i in range(n):
        numerator += (X[i] - mean_x)*(Y[i] - mean_y)
        denominator += ((X[i] - mean_x)**2)
    slope = numerator/denominator
    print("Slope of the line is: ", slope)

    intercept = mean_y - slope*mean_x
    print("Intercept is: ", intercept)

    print("Regression Equation is: ")
    print(f"Y = ({slope})X + {intercept}")

    X_new = float(input("Enter the X coordinate: "))

    Y_new = slope*X_new + intercept

    print(f"Predicted Y for X = {X_new} is: {Y_new}")

if __name__ == "__main__":
    main()