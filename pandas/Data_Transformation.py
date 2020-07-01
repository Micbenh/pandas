import numpy as np
import pandas as pd

data = pd.DataFrame({'k1':['one','two'] * 3 + ['two'], 'k2':[1,1,2,3,3,4,4]})
print(data)
print()
print(data.duplicated())
print()
print(data.drop_duplicates())
print()
data['v1'] = range(7)
print(data)
print()
print(data.drop_duplicates(['k1']))
print()
print(data.drop_duplicates(['k1','k2'], keep='last'))
print()

print()
print("=============")
print()

#Transforming Data Using a Function or Mapping
data = pd.DataFrame({'food': ['bacon', 'pulled pork', 'bacon',
'Pastrami', 'corned beef', 'Bacon',
'pastrami', 'honey ham', 'nova lox'],
'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
print(data)
print()
meat_to_animal = {'bacon':'pig',
'pulled pork':'pig',
'pastrami':'cow',
'corned beef':'cow',
'honey ham':'pig',
'nova lox':'salmon'}
print(meat_to_animal)
print()

lowercased = data['food'].str.lower()
print(lowercased)
print()

data['animal'] = lowercased.map(meat_to_animal)
print(data)
data['food'].map(lambda x: meat_to_animal[x.lower()])
print(data)

print()
print("=============")
print()

#Replacing Values
data = pd.Series([1., -999., 2., -999., -1000., 3.])
print(data)
print()
data = data.replace(-999, np.nan)
print(data)
print()
data = data.replace([-999, -1000], np.nan)
print(data)
print()
data = data.replace([-999, -1000], [np.nan, 0])
print(data)
print()
data = data.replace({-999: np.nan, -1000: 0})
print(data)
print()

# Renaming Axis Indexes
print()
print("=============")
print()

data = pd.DataFrame(np.arange(12).reshape((3, 4)),
index=['Ohio', 'Colorado', 'New York'],
columns=['one', 'two', 'three', 'four'])
print(data)
print()
transform = lambda x: x[:4].upper()
data = data.index.map(transform)
print(data)
print()
print()
print("=============")
print()

# Detecting and Filtering Outliers
data = pd.DataFrame(np.random.randn(1000,4))
print(data)
print()
print(data.describe())
print()
col = data[2]
print(col)
print()
print(col[np.abs(col) > 3])
print()
print(data[(np.abs(data) > 3).any(1)])

print()
print("=============")
print()
# Permutation and Random Sampling
df = pd.DataFrame(np.arange(5 * 4).reshape((5, 4)))
print(df)
sampler = np.random.permutation(5)
print()
print(sampler)
print()
print(df.take(sampler))
print()
print(df.sample(n=3))

print()
print("=============")
print()

# Computing Indicator/Dummy Variables
df = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],
'data1': range(6)})
print(df)
print()
print(pd.get_dummies(df['key']))
print()
dummies = pd.get_dummies(df['key'], prefix='key')
print(dummies)
print()
df_with_dummies = df[['data1']].join(dummies)
print(df_with_dummies)
print()


