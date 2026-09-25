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
    # print(df)
    # obj = df.describe()
    # print(obj)

    df['Total'] = df['Math'] + df['Science'] + df['English']
    print(df)
    # print(df[df['Science']>85])
    # df['Name'] = df['Name'].replace('Pooja','Puja')
    # df = df.sort_values(by='Total')
    # print(df)

    # plt.bar(
    #     df['Name'],
    #     df['Total']
    # )
    # plt.title("Name vs Total marks Bar graph")
    # plt.xlabel("Name")
    # plt.ylabel("Total marks")
    # plt.show()

    # plt.plot(
    #     'Marks',
    #     'Subjects'
    # )

    # subjects = ['Math','Science','English']
    # marks = df[df["Name"] == 'Amit'][subjects].iloc[0]

    # plt.plot(subjects,marks, marker='o')
    # plt.xlabel("Subjects")
    # plt.ylabel("Marks")
    # plt.title("Amit's marks across all subjects")
    # plt.grid(True)
    # plt.show()

    # data2 = {
    #     'Name': ['Amit','Sagar','Pooja'],
    #     'Math':[np.nan,76,88],
    #     'Science':[91,np.nan,85]
    # }
    # df2 = pd.DataFrame(data2)

    # df2['Math'] = df2['Math'].fillna(df2['Math'].mean())
    # df2['Science']= df2['Science'].fillna(df2['Science'].mean())
    # print(df2)

    df = df.drop('English',axis=1)
    print(df)
    
if __name__ == "__main__":
    main()
