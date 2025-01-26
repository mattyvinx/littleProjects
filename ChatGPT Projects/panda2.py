import pandas as pd

df=pd.read_excel("sales_data.xlsx")
print(df.groupby("Product")["Price"].mean())