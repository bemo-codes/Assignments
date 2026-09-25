import math
import matplotlib.pyplot as plt
import numpy as np

def main():
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    n = len(X)

    sum_x = 0
    for i in X:
        sum_x +=i
    print("Sum is: ", sum_x)
    mean_x = sum_x/n
    print("Mean of X is: ", mean_x)
    sum_y = 0
    for i in Y:
        sum_y +=i
    print("Sum is: ", sum_y)
    mean_y = sum_y/n
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

    # X_new = float(input("Enter the X coordinate: "))

    # Y_new = slope*X_new + intercept

    # print(f"Predicted Y for X = {X_new} is: {Y_new}")

    Y_preds =[]
    for i in X:
        Y_new = slope*i + intercept
        Y_preds.append(Y_new)
        print(f"Predicted Y for X = {i} is: {Y_new}")
    print(Y_preds)

    for i,j in zip(Y,Y_preds):
        MSE = (i - j)**2 / n
        print(f"MSE for Y = {i} is: {MSE}")

    num = 0
    deno = 0
    for i,j in zip(Y,Y_preds):
        num += (i - j)**2
        deno += (i - mean_y)**2
    R2 = 1 - num/deno
    print("R2 = ", R2)


if __name__ == "__main__":
    main()