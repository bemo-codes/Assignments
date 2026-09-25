actual = [1,1,1,1,0,0,0,0]
predicted = [1,1,0,1,0,1,0,0]

TP = 0
TN = 0
FN = 0
FP = 0

for act, pre in zip(actual, predicted):
    if act == 1:
        if pre == act:
            TP += 1
        else: 
            FP +=1

    if act == 0: 
        if pre == act:
            TN += 1
        else:
            FN += 1

print("True postive is: ", TP)
print("False postive is: ", FP)
print("True Negative is: ", TN)
print("False Negative is: ", FN)
