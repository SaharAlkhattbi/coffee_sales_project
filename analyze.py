"Coffee Sales Analysis" 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the dataset
df = pd.read_csv("CoffeeBeansSales.csv")

# Display the first 5 rows
print("🔹 First 5 rows:")
print(df.head())

# Display dataset info
print("\n🔹 Dataset Info:")
print(df.info())

# Display statistical summary
print("\n🔹 Descriptive Statistics:")
print(df.describe())

# Plot total sales by city
plt.figure(figsize=(10, 6))
sns.barplot(x="City", y="Final Sales", data=df, estimator=sum, ci=None)
plt.title("Total Sales by City")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
