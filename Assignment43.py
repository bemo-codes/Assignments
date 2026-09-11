import numpy as np
import pandas as pd

from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder


def main():
    df = pd.read_csv("PlayPredictor.csv")

    df.drop(columns=["Unnamed: 0"], inplace=True)

    X = df.drop('Play', axis=1)
    Y = df['Play']

    encoders = {}

    for column in X.columns:                                
        encoder = LabelEncoder()
        X[column] = encoder.fit_transform(X[column])                #As the KNN doesnt understand strings we have to encode the given data
        encoders[column] = encoder

    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X,Y)

    new = pd.DataFrame({
        'Whether': ['Sunny'],
        'Temperature': ['Hot']
    })

    for column in new.columns:
        new[column] = encoders[column].transform(new[column])           #here we have to transform the new column into encoded column as we did previously
    
    Y_pred = model.predict(new)
    print("Prediction is: ", Y_pred)

if __name__ == "__main__":
    main()