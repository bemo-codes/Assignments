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

    model = DecisionTreeClassifier()
    model.fit(X_train, Y_train)

    new_df = {
        "StudyHours": [3,5,7,8,9,4],
        "Attendance": [63,70,86,90,67,90],
        "PreviousScore": [44,55,67,77,87,90],
        "AssignmentsCompleted":[3,4,5,6,7,8],
        "SleepHours": [5,5,6,7,8,8]
    }
    dobj = pd.DataFrame(new_df)
   
    for feature, score in zip(X.columns, model.feature_importances_):
        print(f"{feature} : {score}")

    Y_pred_test = model.predict(dobj)

    for i in range(len(Y_test)):
        if Y_pred_test[i] == 1:
            result = "Pass"
        else:
            result ="Fail"
        print(f"Student {i+1}: {result}")   

    correct = 0
    for i in range(len(Y_test)):
        if Y_pred_test[i] == Y_test.iloc[i]:
            correct += 1 

    Maccuracy = (correct/len(Y_test)) * 100

    print("Manual Accuracy is: ", Maccuracy)   

if __name__ == "__main__":
    main()