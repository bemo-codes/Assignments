import pandas as pd

from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

def main():
    #####################################
    #Step-1: Load the dataset
    #####################################
    df = pd.read_csv("WinePredictor.csv")

    #####################################
    #Step-2: Clean dataset
    #####################################

    df.dropna(inplace = True)
    print("Shape of dataset: ", df.shape)
    print("Total records: ", df.shape[0])
    print("Total columns: ", df.shape[1])

    #####################################
    #Step-3: Separate independent and dependent variables
    #####################################

    X = df.drop('Class', axis=1)
    Y = df['Class']

    #####################################
    #Step-4: Split the dataset
    #####################################

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=42, test_size=0.2)

    #####################################
    #Step-5: Scale the features
    #####################################
    
    scalar = StandardScaler()
    X_train = scalar.fit_transform(X_train)
    X_test = scalar.fit_transform(X_test)
    
    #####################################
    #Step-6: Declare and train the model
    #####################################

    model = KNeighborsClassifier()
    model.fit(X_train, Y_train)
    Y_pred = model.predict(X_test)

    print("Accuracy is: ", accuracy_score(Y_pred, Y_test)*100)
    print("Confusion matrix: ")
    print(confusion_matrix(Y_pred,Y_test))



if __name__ == "__main__":
    main()