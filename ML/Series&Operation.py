import numpy as np
import pandas as pd
df=pd.read_csv("C:/Users/admin/Desktop/DataScience with python/ML/Cricket_Players.csv")
print(df.describe())
print(df.describe(include='all'))