import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("sales_data_100.csv")

summary = df.pivot_table(index="Region",columns="Category",values="Quantity",aggfunc="sum",fill_value=0)
summary.plot(kind="bar",figsize=(14,6))
plt.show()