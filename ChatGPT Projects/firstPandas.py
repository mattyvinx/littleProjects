import pandas as pd

df=pd.read_excel("sales_data.xlsx")
totalSales = df['Total Sales'].sum()
print(f"The total sales for all items totals ${totalSales}")

print(f'The top selling item is {df["Product"][df["Quantity"].idxmax()]}.')

