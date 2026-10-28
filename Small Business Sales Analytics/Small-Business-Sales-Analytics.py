"""Level 2 — Intermediate Analyst Project
Small Business Sales Analytics

Imagine you're analyzing a shop's sales data."""

import pandas as pd
import matplotlib.pyplot as plt

#Tasks
df = pd.read_csv("business_sales.csv")

#-Revenue column
df["Revenue"] = df["Price"] * df["Quantity"]

#print(df["Revenue"].sum())  #   Total revenue
#print(df.groupby("Product")["Quantity"].sum())  #   Best selling product

#Visualization
sales = df.groupby("Product")["Revenue"].sum()
sales.plot(kind="bar")
plt.title("Revenue per Product")

#Advanced Analysis
#-Daily revenue trend:
daily = df.groupby("Date")["Revenue"].sum()
#daily.title("Daily Revenue Trend")
daily.plot(kind="bar")

#AIzaSyApmzOZzwGszRrbhBP61Em4IXgIRmOfRf8
plt.show()