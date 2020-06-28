import pandas as pd
import numpy as np

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}

print(data)
print()

#to data frame
df = pd.DataFrame(data)
print(df)
print()

# top 5
print(df.head())
print()

#self chosen colmn names
print(pd.DataFrame(data, columns=['yEaR','state','pop']))
print()

#self chosen index names
df2 = pd.DataFrame(data, columns=['year','state','pop','debt'], index=['one','two','three','four','five','six'])
print(df2)
print(df2.columns)
print(df2.state)

