import pandas as pd
import numpy as np 

#Series
obj = pd.Series([4,7,-5,3])
print(obj)
print()
print(obj.values)
print()

#Series with index
obj2  = pd.Series([4,7,-5,3], index = ['d', 'b', 'a', 'c'])
print(obj2)
print()
print(obj2.index)
print()
print(obj2['a'])
print()
print(obj2[['c','a','d']])

#bool filtering
print("BOOL")
print(obj2[obj2 > 0])
print()
print(obj2 * 2)
print()
print(np.exp(obj2))
print()
print('b' in obj2)
print('h' in obj2)
print()

#dict to Series
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = pd.Series(sdata)
print(obj3)
print()
states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = pd.Series(obj3, index=states)
print(obj4)
print()
print(pd.isnull(obj4))
print(obj4.isnull())
print()

#concat
print(obj3 + obj4)
print()
obj4.name = 'Population'
obj4.index.name = 'state'
print(obj4)

