import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("C:/Users/hp/Downloads/archive/sales_data_sample.csv", encoding="ISO-8859-1")

# Basic Analysis: Average Price and Sales
average_price = df["PRICEEACH"].mean()
average_sales = df["SALES"].mean()

print(f"Average Product Price: ${average_price:.2f}")
print(f"Average Sales per Order: ${average_sales:.2f}")

# Visualization 1: Bar Chart - Top 10 Products by Sales
plt.figure(figsize=(12, 6))
top_products = df.groupby("PRODUCTLINE")["SALES"].sum().nlargest(10)
sns.barplot(x=top_products.index, y=top_products.values, palette="coolwarm")
plt.title("Top 10 Product Lines by Total Sales")
plt.xticks(rotation=45)
plt.ylabel("Total Sales ($)")
plt.show()

# Visualization 2: Scatter Plot - Price vs Quantity Ordered
plt.figure(figsize=(8, 5))
sns.scatterplot(x="PRICEEACH", y="QUANTITYORDERED", data=df, color="blue", s=100)
plt.title("Price vs Quantity Ordered")
plt.xlabel("Price Each ($)")
plt.ylabel("Quantity Ordered")
plt.grid(True)
plt.show()

# Visualization 3: Heatmap - Correlation Matrix
plt.figure(figsize=(6, 4))
numeric_df = df.select_dtypes(include=["number"])
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()
