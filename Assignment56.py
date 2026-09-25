import pandas as pd
import numpy as np

from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, VotingClassifier, BaggingClassifier

df = pd.read_csv("Fraudulent_Transaction_Detection.csv")
df = df.dropna()
print(df.shape)
print(df.head())

X = df.drop("Fraud", axis=1)
Y = df['Fraud']

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2, random_state=42)

model_dt = DecisionTreeClassifier(random_state=42)
model_dt.fit(X_train, Y_train)
Y_pred = model_dt.predict(X_test)

print("Accuracy of Decision tree is: ", accuracy_score(Y_pred, Y_test)*100)
print("Precision Score is: ", precision_score(Y_pred,Y_test))
print("Recall score is: ", recall_score(Y_pred, Y_test))
print("F1 score is: ", f1_score(Y_pred, Y_test))
print("Confuison matix is: ")
print(confusion_matrix(Y_pred, Y_test))
print("\n\n\n")

model_bg = BaggingClassifier(
    estimator=model_dt,
    n_estimators=10,
    random_state=42
)

model_bg = BaggingClassifier(random_state=42)
model_bg.fit(X_train, Y_train)
Y_pred_bg = model_bg.predict(X_test)

print("Accuracy of Bagging Classifier is: ", accuracy_score(Y_pred_bg, Y_test)*100)
print("Precision Score is: ", precision_score(Y_pred_bg,Y_test))
print("Recall score is: ", recall_score(Y_pred_bg, Y_test))
print("F1 score is: ", f1_score(Y_pred_bg, Y_test))
print("Confuison matix is: ")
print(confusion_matrix(Y_pred_bg, Y_test))
print("\n\n\n")


model_ada = AdaBoostClassifier(
    n_estimators=50,
    learning_rate=1.0,
    random_state=42
)

model_ada = AdaBoostClassifier(random_state=42)
model_ada.fit(X_train, Y_train)
Y_pred_ada = model_ada.predict(X_test)

print("Accuracy of AdaBoost Classifier is: ", accuracy_score(Y_pred_ada, Y_test)*100)
print("Precision Score is: ", precision_score(Y_pred_ada,Y_test))
print("Recall score is: ", recall_score(Y_pred_ada, Y_test))
print("F1 score is: ", f1_score(Y_pred_ada, Y_test))
print("Confuison matix is: ")
print(confusion_matrix(Y_pred_ada, Y_test))
print("\n\n\n")

model_rf = RandomForestClassifier(
    n_estimators=10,
    random_state=42
)

model_rf = RandomForestClassifier(random_state=42)
model_rf.fit(X_train, Y_train)
Y_pred_rf = model_rf.predict(X_test)

print("Accuracy of RandomForest Classifier is: ", accuracy_score(Y_pred_rf, Y_test)*100)
print("Precision Score is: ", precision_score(Y_pred_rf,Y_test))
print("Recall score is: ", recall_score(Y_pred_rf, Y_test))
print("F1 score is: ", f1_score(Y_pred_rf, Y_test))
print("Confuison matix is: ")
print(confusion_matrix(Y_pred_rf, Y_test))
print("\n\n\n")

model_vot = VotingClassifier(
    estimators=[
        ('dt', model_dt),
        ('bg', model_bg),
        ('ada', model_ada),
        ('rf', model_rf)
    ],
    voting='hard'
)

model_vot.fit(X_train, Y_train)
Y_pred_vot = model_vot.predict(X_test)

print("Accuracy of Voting Classifier is: ", accuracy_score(Y_pred_vot, Y_test)*100)
print("Precision Score is: ", precision_score(Y_pred_vot,Y_test))
print("Recall score is: ", recall_score(Y_pred_vot, Y_test))
print("F1 score is: ", f1_score(Y_pred_vot, Y_test))
print("Confuison matix is: ")
print(confusion_matrix(Y_pred_vot, Y_test))
print("\n\n\n")
