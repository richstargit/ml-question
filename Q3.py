import numpy as np
import pandas as pd

df = pd.read_csv("sales_data_100.csv")
print(df.loc[(df["Price"]>1000) & (df["Category"]=="Furniture")])
print("--------------------------------------------------------------")
print(df.loc[(df["OrderDate"]>="2024-02-01")&((df["Region"]=="North")|(df["Region"]=="Central"))])