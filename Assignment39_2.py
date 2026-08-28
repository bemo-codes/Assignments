import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

def main():
    df = pd.read_csv("student_performance_ml.csv")

    X = df.drop("FinalResult", axis=1)
    Y = df["FinalResult"]

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42
    )
    model = DecisionTreeClassifier()
    model.fit(X_train, Y_train) 

    Y_pred = model.predict(X_test)

    for i, j in zip(Y_test, Y_pred):
        print(f"Acutual ouput: {i} \n predicted output: {j}")

if __name__ == "__main__":
    main()

