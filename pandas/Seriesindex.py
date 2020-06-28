import pandas as pd
import numpy as np

#series droping
obj = pd.Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
print()
print(obj)
print()
new_obj = obj.drop('c')
print(new_obj)
print()
print(obj.drop(['d','c']))
print()

#df droping
data = pd.DataFrame(np.arange(16).reshape((4, 4)),
index=['Ohio', 'Colorado', 'Utah', 'New York'],
columns=['one', 'two', 'three', 'four'])
print(data)
print()

print(data.drop(['Colorado','Ohio']))
print()
print(data.drop('two',axis=1))
print()
print(data.drop(['two','four'], axis='columns'))
print()

#Series Selection 
obj = pd.Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
print(obj)
print()
print(obj['b'])
print()
print(obj[0])
print()
print(obj[2:4])
print()
print(obj[['b','a','d']])
print()
print(obj[[1,3]])
print()
print(obj[obj < 2])
print()

#DF Selection
data = pd.DataFrame(np.arange(16).reshape((4, 4)),
index=['Ohio', 'Colorado', 'Utah', 'New York'],
columns=['one', 'two', 'three', 'four'])
print(data)
print()
print(data['two'])
print()
print(data[['three','one']])
print()
print(data[:3])
print()
print(data[data['three'] > 5])
print()
print(data < 5)
print()

#loc iloc
print(data.loc['Colorado', ['two','three']])
print()
print(data.iloc[2])
print()
print(data.iloc[[1, 2], [3, 0, 1]])
print()
print(data.loc[:'Utah', 'two'])
print()
print(data.iloc[:, :3][data.three > 5])
print()








