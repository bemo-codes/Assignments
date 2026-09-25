import pandas as pd
import numpy as np


from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

def main():

    df = pd.DataFrame({
        'studyhour':[2,5,6,1],
        'attendance':[60,80,85,50],
        'result':['Fail','Pass','Pass','Fail']
    })

    X = df[['studyhour', 'attendance']]
    Y = df['result']

    X_new = float(input("Enter the number of study hours: "))
    Y_new = float(input("Enter the attendance: "))

    new_point = np.array([[X_new, Y_new]])

    model = KNeighborsClassifier(n_neighbors=2)
    model.fit(X,Y)

    prediction = model.predict(new_point)
    print("Prediction is: ",prediction)   

if __name__ == "__main__":
    main()

#This model is overfitting 