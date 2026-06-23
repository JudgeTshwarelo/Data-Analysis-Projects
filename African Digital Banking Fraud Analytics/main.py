#Senoamadi Financial Services Fraud Analytics

#Find:
    #Fraud
    #Suspicious users
    #Revenue trends

#Data Cleaning
#Fix:
    #-Missing values
    #-Duplicate transactions
    #-Invalid provinces
    #-Negative transaction amounts

#Tasks
import pandas as pd

df = pd.read_csv("reports/bank_dataset.csv")    #load data

#Clean Data
df["Province"] = df["Province"].replace({"lim": "Limpopo"})     # Fix province names
df = df.fillna({"Amount": 0}) #   Fill missing values
df = df[df["Amount"] >= 0]   #   Remove negative weights


#Analytics

#Calculate:
#Revenue
revenue = df.groupby("Transaction_Type")["Amount"].sum()
#print(f"Total Transfer: R{revenue["Transfer"].round()}")    #Total Transfer
#print(f"Total Deposits: R{revenue["Deposit"].round()}")    #Total deposits
#print(f"Total Withdrawals: R{revenue["Withdrawal"].round()}")    #Total withdrawals

#Customer Insights
#Top:
top_customers = (df.groupby("Customer_ID")["Amount"].sum()
                    .sort_values(ascending=False)
                    .head(10)
                 )      #10 customers - by transaction value.
#print(top_customers)

#Fraud Analysis
#Find:
fraud_rate = df.groupby("Province")["Fraud"]    #Fraud Rate - per province.
#print(fraud_rate.sum())

#Visualization
#1. Transaction Types
import matplotlib.pyplot as plt
import numpy as np

categories = ["Transfer", "Deposit", "Withdrawal"]
values = np.array([revenue["Transfer"],
              revenue["Deposit"],
              revenue["Withdrawal"]
              ])
colors = ["Blue", "Red", "Green"]

plt.pie(values, labels=categories,
                autopct="%1.1f%%",
                colors=colors,
                explode=[0, 0, 0.2],
                shadow=True)

plt.title("Transaction Types")    #Pie Chart

plt.show()


#2. Transaction Distribution
    #Histogram
plt.figure(figsize=(8, 5))
plt.hist(df["Amount"], bins=20)
plt.title("Transaction Distribution")
plt.xlabel("Transaction Amount")
plt.ylabel("Frequency")
plt.show()

#3. Fraud vs Non-Fraud
    #Bar Chart
fraud_counts = df["Fraud"].value_counts()

plt.figure(figsize=(6, 4))
fraud_counts.plot(kind="bar")
plt.title("Fraud vs Non-Fraud Transactions")
plt.xlabel("Fraud")
plt.ylabel("Count")
plt.show()

#4. Revenue per Province
    #Line Graph
province_revenue = df.groupby("Province")["Amount"].sum()

plt.figure(figsize=(10, 5))
province_revenue.plot(kind="line", marker="o")

plt.title("Revenue per Province")
plt.xlabel("Province")
plt.ylabel("Revenue")

plt.show()

#5. Customer Spending
    #Scatter Plot
customer_spending = (df.groupby("Customer_ID")["Amount"].sum().reset_index())

plt.figure(figsize=(8, 5))
plt.scatter(customer_spending["Customer_ID"],
            customer_spending["Amount"])
plt.title("Customer Spending")
plt.xlabel("Customer ID")
plt.ylabel("Total Spending")
plt.show()

#Extra Challenge (Portfolio Killer)
#Create a final script:
    #python main.py

#that automatically:
    #1. Loads data
    #2. Cleans data
    #3. Generates statistics
    #4. Saves graphs
    #5. Exports reports

#Output:
#reports/
    #cleaned_data.csv
    #fraud_summary.csv
    #mortality_summary.csv
#graphs/
    #chart1.png
    #chart2.png
    #chart3.png