import numpy as np
import pandas as pd
list =[[1,'Virat',18],[2,'Rohit',45]]
df=pd.DataFrame(list)
df.columns=['S.no','Name','Number']
df.info()
df=pd.read_csv("C:\Users\admin\Desktop\DataScience with python\ML\Cricket_Players.csv")
print(df)