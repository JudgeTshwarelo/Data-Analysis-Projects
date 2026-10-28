"""Advanced Analyst Project
Student Accommodation Market Analyzer

This is perfect for your UL accommodation idea."""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Student-Market.csv")

#Analysis Ideas
#   Cheapest accommodation
#   Average price
df.sort_values(by="Price")
print(df["Price"].mean())
#Visualization
#   Distance vs price

plt.scatter(df["DistanceFromCampus"], df["Price"])

plt.xlabel("Distance from campus")
plt.ylabel("Price")
plt.show()