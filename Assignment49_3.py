import pandas as pd

from sklearn.preprocessing import StandardScaler
data = [[25, 20000],
        [30, 40000],
        [35, 80000]]

df = pd.DataFrame(data)

scalar = StandardScaler()
data = scalar.fit_transform(data)
print(data)
