import pandas as pd
import numpy as np

#Finding and dropping missing values
string_data = pd.Series(['aardvark','artichoke',np.nan, 'avocado'])
print(string_data)
print()
print(string_data.isnull())
print()
string_data[0] = None
print(string_data.isnull())
print()
print("=============")
print()

data = pd.Series([1, np.nan, 3.5, np.nan, 7])
print(data)
print()
print(data.dropna())
print()
print(data[data.notnull()])
print("=============")
print()

data = pd.DataFrame([[1., 6.5, 3.], [1., np.nan, np.nan],[np.nan, np.nan, np.nan], [np.nan, 6.5, 3.]])
print(data)
print()
total_clean = data.dropna()
print(total_clean)
print()
partialy_clean = data.dropna(how='all')
print(partialy_clean)
print()

#column
data[4] = np.nan
print(data)
print()
data = data.dropna(axis=1, how='all')
print(data)

print("=============")
print()
print()

df = pd.DataFrame(np.random.randn(7,3))
print(df)
print()
print(df.iloc[:4, 1])
df.iloc[:4, 1] = np.nan
print(df)
print()
print(df.iloc[:2, 2])
print()
df.iloc[:2, 2] = np.nan
print(df)
print()
df = df.dropna(thresh=2)
print(df)

#Filling Missing values
print()
print("=============")
print()
df.iloc[:4, 1] = np.nan
df.iloc[:2, 2] = np.nan
df = df.fillna(0)
print(df)
print()
df = df.fillna({1: 0.5, 2: 0})
print(df)
print()
_ = df.fillna(0, inplace=True)
print(df)

print()
print("=============")
print()

df = pd.DataFrame(np.random.randn(6, 3))
print(df)
print()
df.iloc[2:, 1] = np.nan
df.iloc[4:, 2] = np.nan
print(df)
print()
print(df.fillna(method='ffill'))
print()
print(df.fillna(method="ffill", limit=2))
print()

data = pd.Series([1., np.nan, 3.5, np.nan, 7])
print(data)
print(data.fillna(data.mean()))

