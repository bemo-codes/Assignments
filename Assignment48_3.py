import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def main():
    data = {
        'Experience':[1,2,3,4,5],
        'Salary': [20000, 25000, 30000, 35000, 40000]
    }
    df = pd.DataFrame(data)
    X = df.drop("Salary", axis=1)
    Y = df['Salary']

    model = LinearRegression()
    model.fit(X,Y)
    Y_pred = model.predict([[6]])

    print("Predicted salary for 6 years of experience is: ", Y_pred)

if __name__ == "__main__":
    main()