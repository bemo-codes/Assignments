from sklearn.metrics import classification_report, confusion_matrix

actual = [1,1,1,1,0,0,0,0]
predicted = [1,1,0,1,0,1,0,0]

print("Classification report: \n")
print(classification_report(actual, predicted))

print("Confusion Matrix: \n")
print(confusion_matrix(actual, predicted))