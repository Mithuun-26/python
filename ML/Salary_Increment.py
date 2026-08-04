import numpy as np
import pandas as pd

def cal_sal(Experience_Years, Salary):
    inc = 0
    if Experience_Years >= 10:
        if Salary >= 300000:
            inc = (Salary * 30) / 1500
        else:
            inc = 7000
    elif Experience_Years >= 5:
        if Salary >= 150000:
            inc = (Salary * 30) / 3000
        else:
            inc = 3000
    else:
        inc = 1000
    return inc

df = pd.read_csv("ML/Employee_Salary_Dataset.csv")
df["Annual Salary"] = df["Salary"] * 12
df["Increment"] = df.apply(
    lambda row: cal_sal(row["Experience_Years"], row["Salary"]),
    axis=1
)
df["Updated_Sal_with_Increment"] = df["Salary"] + df["Increment"]
df.info()
print(df)