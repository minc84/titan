import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mpl

trd = pd.read_csv('train.csv')
tsd = pd.read_csv('test.csv')

td = pd.concat([trd, tsd], ignore_index=True, sort  = False)
td1 = td.shape
print(td1)