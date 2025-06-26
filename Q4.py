import numpy as np
import pandas as pd

df = pd.read_csv("sales_data_100.csv")
print("1.--------------------------------------------------------------")
print(df.iloc[:10])
print("2.--------------------------------------------------------------")
print(df.loc[df["Price"] == df["Price"].max()])
print(df["Price"].mean())
print("3.--------------------------------------------------------------")
df["TotalPrice"] = df["Price"]*df["Quantity"]
print(df)
print("4.--------------------------------------------------------------")
df["Discount"]=5
for i in range(len(df)):
    if df.loc[i,"Category"]=="IT":
        df.loc[i,"Discount"]=10

print(df)
print("5.--------------------------------------------------------------")
df["NetPrice"]=df["TotalPrice"]*(1-df["Discount"]/100)
print(df)

print("6.--------------------------------------------------------------")
print(df.groupby("Category")["TotalPrice"].sum())
print("7.--------------------------------------------------------------")
print(df.groupby("Region")["Quantity"].sum())
print("8.--------------------------------------------------------------")
df = df.groupby("Product")["Quantity"].sum().sort_values(ascending=False)
print(df.iloc[:5])
print("---")
print(df.iloc[len(df)-5:len(df)])
print("9.--------------------------------------------------------------")
print(df[df<5])