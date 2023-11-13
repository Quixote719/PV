import numpy as np
import pandas as pd

list1 = [1,2,3,4]
list2 = [5,6,7,8]
list = [list1, list2]
array1 = np.array(list1)
arrayl = np.array(list)
print(list1, array1, list, arrayl)

print(arrayl[1][3])

# Create a Series using a NumPy array of ages but customize the indices to be the names that correspond to each age
ages = np.array([13,25,19,8])
series1 = pd.Series(ages,index=['Lucas', 'Emma', 'Serajh', 'Thor'])
print(series1, series1.iloc[1])