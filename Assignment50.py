import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_breast_cancer

def main():
    cancer = load_breast_cancer(as_frame=True)
    df = cancer.frame
    print(df.head())
    print(df.describe())

    df = df.dropna()
    X = df.drop('target', axis=1)
    Y = df['target']

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42
    )
    scalar = StandardScaler()
    X_train = scalar.fit_transform(X_train)
    X_test = scalar.fit_transform(X_test)

    model = KNeighborsClassifier(n_neighbors=2)
    model.fit(X_train, Y_train)
    Y_pred = model.predict(X_test)

    print("Accuracy is: ", accuracy_score(Y_pred, Y_test)*100)
    print("Confusion Matrix: ", confusion_matrix(Y_pred, Y_test))
    print("Precision Score: ", precision_score(Y_pred, Y_test))
    print("Recall score: ", recall_score(Y_pred, Y_test))
    print("F1 score: ", f1_score(Y_pred, Y_test))

if __name__ == "__main__":
    main()