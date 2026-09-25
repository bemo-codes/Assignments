import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

def main():

    df = pd.read_csv("student_performance_ml.csv")
    print(df)

    X = df.drop(columns=["FinalResult"])
    Y = df["FinalResult"]
    
    print(X.shape)
    print(Y.shape)

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        random_state=42,
        test_size=0.2
    )
    model = DecisionTreeClassifier(random_state=0)
    model.fit(X_train, Y_train)
    Y_pred = model.predict(X_test)
    Accuracy = accuracy_score(Y_pred, Y_test)*100

    model1 = DecisionTreeClassifier(random_state=0)
    model1.fit(X_train, Y_train)
    Y_pred = model1.predict(X_test)
    Accuracy1 = accuracy_score(Y_pred, Y_test)*100

    model2 = DecisionTreeClassifier(random_state=0)
    model2.fit(X_train, Y_train)
    Y_pred = model2.predict(X_test)
    Accuracy2 = accuracy_score(Y_pred, Y_test)*100

    print(
        f"Accuracy of rf = 0 {Accuracy} \n",
        f"Accuracy of rf = 10 {Accuracy1} \n",
        f"Accuracy of rf = 42 {Accuracy2} \n"    
        )

if __name__ == "__main__":
    main()


