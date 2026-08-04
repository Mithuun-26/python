import numpy as np
import pandas as pd
def cal_sal(Salary):
    inc = 0
    if Salary>=20000:
        inc = (Salary*30)/100
    else:
        inc = 3000
    return inc
df=pd.read_csv("ML\Employee_Salary_Dataset.csv")
print(df.info())
#print(df.Salary.median)
df["Annual Salary"]=df.Salary*12
df["Increment"]=df.Salary.apply(cal_sal)
df["Updated_Sal_with_Increment"]=df["Salary"]+df["Increment"]
print(df)