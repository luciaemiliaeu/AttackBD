import pandas as pd 
from pandas.errors import ParserError

d2 = pd.read_csv('bruteforceclean3.csv', sep=',', error_bad_lines=False)
d2.dropna(axis ='columns', thresh = d2.shape[0]*0.5, inplace = True)
d2.drop_duplicates(inplace = True)
d2['label'].dtypes()
print(d2['label'].dtypes)