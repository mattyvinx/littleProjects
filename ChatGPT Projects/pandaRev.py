import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("revenue_cycle_data.xlsx")

grouped_data = df.groupby("Patient ID")["Charge Amount"].sum().reset_index()
plt.bar(grouped_data["Patient ID"], grouped_data["Charge Amount"])
plt.xlabel("Patient ID")
plt.ylabel("Total Charges")
plt.title("Total Charges by Patient")
plt.show()