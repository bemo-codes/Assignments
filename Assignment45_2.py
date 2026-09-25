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

    df['Math'] = (
        (df['Math'] - df['Math'].min())/
    (df['Math'].max() - df['Math'].min())
    )

    df['Gender'] = ['Male','Male','Female']
    df = pd.get_dummies(df, columns=['Gender'], dtype=int)
    print(df)
    
if __name__ == "__main__":
    main()
