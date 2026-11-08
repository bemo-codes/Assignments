import pandas as pd 

from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt


new_employees = pd.DataFrame({
    'Age': [30, 25, 45, 28, 35],
    'MonthlyIncome': [80000, 35000, 120000, 45000, 70000],
    'YearsAtCompany': [5, 1, 15, 3, 8],
    'TotalWorkingYears': [8, 2, 20, 5, 12],
    'DistanceFromHome': [20, 5, 10, 25, 7],
    'JobSatisfaction': [3, 2, 4, 2, 4],
    'WorkLifeBalance': [2, 3, 4, 2, 3],
    'OverTime': ['Yes', 'No', 'No', 'Yes', 'No'],
    'NumCompaniesWorked': [3, 1, 2, 4, 2],
    'TrainingTimesLastYear': [3, 2, 4, 2, 3]
})

def main():
    global model, scalar

    df = pd.read_csv("Employee_Attrition.csv")
    print(df.shape)
    print(df.columns)
    print(df.head())

    print("Number of null values: \n", df.isnull().sum())

    numeric_features = df.select_dtypes(include=['int64', 'float64']).columns
    categorical_features = df.select_dtypes(include=['object']).columns

    df = df.dropna()

    print("Numerical Features:")
    print(numeric_features)

    print("\nCategorical Features:")
    print(categorical_features)

    df = pd.get_dummies(
        df, 
        columns=["OverTime", "Attrition"],
        drop_first=True,
        dtype=int               #we used this to convert the output from boolean to integer i.e. 1=true and 0=false
        )

    X = df.drop('Attrition_Yes', axis=1)
    Y = df['Attrition_Yes']

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.3,
        random_state=42
    )

    scalar = StandardScaler()
    X_train_scaled = scalar.fit_transform(X_train)
    X_test_scaled = scalar.transform(X_test)

    model = MLPClassifier(
        hidden_layer_sizes=(4, 2),     #12x12 is causing overfitting
        activation='relu',
        solver='adam',
        max_iter=1000,
        random_state=42
    )

    model = model.fit(X_train_scaled, Y_train)  

    print("Number of iterations:", model.n_iter_)

    Y_pred_train = model.predict(X_train_scaled)
    Y_pred = model.predict(X_test_scaled)

    print("Accuracy while testing: ", accuracy_score(Y_pred, Y_test)*100)
    print("Accuracy while training: ", accuracy_score(Y_pred_train, Y_train)*100)

    print("Confusion Matrix: ")
    print(confusion_matrix(Y_pred, Y_test))

    plt.plot(model.loss_curve_)
    plt.xlabel("Iterations")
    plt.ylabel("Loss")
    plt.title("MLP loss curve")
    plt.show()

    PredictAttrition(new_employees)

def PredictAttrition(employee_data):

    employee_data = pd.get_dummies(
        employee_data,
        columns=['OverTime'],
        drop_first=True,
        dtype=int
    )

    employee_data = employee_data.reindex(
        columns=feature_columns,
        fill_value=0
    )

    employee_scaled = scalar.transform(employee_data)

    prediction = model.predict(employee_scaled)

    if prediction[0] == 1:
        print("Predicted Attrition: Yes")
    else:
        print("Predicted Attrition: No")
        
if __name__ == "__main__":
    main()