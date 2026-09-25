import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

def main():
    data = {
        'Name':['Amit','Sagar','Pooja'],
        'Math':[85,90,78],
        'Science':[92,88,80],
        'English':[75,85,82]
    }
    df = pd.DataFrame(data)

    # df['Math'] = (
    #     (df['Math'] - df['Math'].min())/
    # (df['Math'].max() - df['Math'].min())
    # )
    # df['Gender'] = ['Male','Male','Female']

    # average_marks = df.groupby('Gender')[['Math','Science','English']].mean()
    # print(average_marks)

    subjects = ['Math','Science','English']
    marks = df[df['Name']=='Sagar'][subjects].iloc[0]

    plt.pie(
        marks,
        labels=subjects,
        autopct='%1.1f%%'
    )
    plt.title("Sagar's subjectwise marks.")
    plt.show()

    
if __name__ == "__main__":
    main()
