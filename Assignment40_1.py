import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

def main():

    df = pd.read_csv("student_performance_ml.csv")
    print(df)

    X = df.drop("FinalResult", axis=1)
    Y = df["FinalResult"]
    
    print(X.shape)
    print(Y.shape)

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        random_state=42,
        test_size=0.2
    )

    model = DecisionTreeClassifier()
    model.fit(X_train, Y_train)

    for feature, score in zip(X.columns, model.feature_importances_):
        print(f"{feature} : {score}")

    Y_pred = model.predict(X_test)

    print("Accuracy is: ", accuracy_score(Y_pred, Y_test)*100)
    

if __name__ == "__main__":
    main()