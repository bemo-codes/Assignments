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
    Y_pred = model.predict(X_test)
    Accuracy = accuracy_score(Y_pred, Y_test)*100

    plt.figure(figsize=(8,2))

    plot_tree(
        model,
        feature_names=X.columns,
        class_names=['Fail','Pass'],
        filled=True
    )
    plt.show()

if __name__ == "__main__":
    main()