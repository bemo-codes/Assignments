import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree

def main():

    df = pd.read_csv("student_performance_ml.csv")
    print(df)

    X = df.drop(columns=["FinalResult"])
    Y = df["FinalResult"]
    df["PerformanceIndex"] = (df["StudyHours"] * 2) + df["Attendance"]    
    print(X.shape)
    print(Y.shape)

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        random_state=42,
        test_size=0.2
    )
    model = DecisionTreeClassifier(max_depth=None)
    model.fit(X_train, Y_train)
    Y_pred_train = model.predict(X_train) 
    Y_pred = model.predict(X_test)
    Accuracy = accuracy_score(Y_pred, Y_test)*100
    accuracy = accuracy_score(Y_pred_train, Y_train)*100

    print("Accuracy during testing is: ", Accuracy)
    print("Accuracy during trainig is: ", accuracy)

if __name__ == "__main__":
    main()