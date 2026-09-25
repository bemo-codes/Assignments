import pandas as pd 
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

def main():
    df = pd.read_csv("Advertising.csv")

    print(df.head())
    if "Unnamed: 0" in df.columns:
        df = df.drop(columns="Unnamed: 0")
    print(df)

    print("Total missing values: ")
    print(df.isnull().sum())

    print("-"*50)
    print("Statistical Summary: ")
    print("-"*50)
    print(df.describe())

    print("-"*50)
    print("Correlation between variables: ")
    print("-"*50)
    print(df.corr)
    print("-"*50)

    X = df.drop('sales', axis=1)
    Y = df['sales']
    print(X.head())
    print(Y.head())

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.5,
        random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, Y_train)
    Y_pred = model.predict(X_test)

    for i, j in zip(Y_pred, Y_test):
        print(f"Predicted: {i} Expected: {j}")

    MSE = mean_squared_error(Y_test, Y_pred)
    RMSE = np.sqrt(MSE)
    R2 = r2_score(Y_test, Y_pred)

    print("Mean squared error: ", MSE)
    print("Root mean squared error: ", RMSE)
    print("R2: ", R2)

if __name__ == "__main__":
    main()