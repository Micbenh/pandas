import pandas as pd
import numpy as np

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}

df2 = pd.DataFrame(data, columns=['year','state','pop','debt'], index=['one','two','three','four','five','six'])
print(df2)
print()
# add values
df2['debt'] = 16.5
print(df2)
df2['debt'] = np.arange(6.)
print(df2)
print()
val = pd.Series([-1.2, -1.5, -1.7], index=['two','four','five'])
df2['debt'] = val
print(df2)
print()

#deleting columns
df2['eastern'] = df2.state == 'Ohio'
print(df2)
del df2['eastern']
