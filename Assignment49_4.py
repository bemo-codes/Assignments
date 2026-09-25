import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
data = np.array([
    [25, 20000],
    [30, 40000],
    [35, 80000]]
)

point1 = data[0]
point2 = data[1]

distance = np.linalg.norm(point1 - point2)

scalar = StandardScaler()
data = scalar.fit_transform(data)

s_point1 = data[0]
s_point2 = data[1]

s_distance = np.linalg.norm(s_point1 - s_point2)

print("Distance before scaling:", distance)
print("Distance after scaling:", s_distance)

#before scaling the distance was a large numrical value and after scaling the value was smaller
#without scaling the feature having large value dominates the distance calculation so 
#we using scaling to make both feature contribute to distance calculation equally