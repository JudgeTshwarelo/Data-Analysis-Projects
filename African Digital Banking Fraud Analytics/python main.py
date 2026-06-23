import pandas as pd
import matplotlib.pyplot as plt

#load data
df = pd.read_csv("reports/bank_dataset.csv")  #filename

print(df.head())

#clean data
df = df.drop_duplicates()   #remove duplicates
df = df.dropna()    #handle missing values
print("Data loaded & cleaned!")

#generate stats
print("\n------------------ Data Table Describtion ------------------")
print(df.describe())

print("\n--- Transaction Type & Total Count---")
print(df["Transaction_Type"].value_counts())

print("\n--- Fraud Summary ---")
print(df["Fraud"].value_counts())

#graphs

#Transaction Distribution
plt.figure()
plt.hist(df["Amount"], bins=20)
plt.title("Transaction Distribution")
plt.savefig("transaction_distribution.png")
plt.close()

#Fraud vs Non-Fraud
plt.figure()
df["Fraud"].value_counts().plot(kind="bar")
plt.title("Fraud vs Non-Fraud")
plt.savefig("fraud_vs_nonfraud.png")
plt.close()


#Revenue per Province
province_revenue = df.groupby("Province")["Amount"].sum()

plt.figure()
province_revenue.plot(kind="bar")
plt.title("Revenue per Province")
plt.savefig("revenue_province.png")
plt.close()


#Revenue per Transaction Type
type_revenue = df.groupby("Transaction_Type")["Amount"].sum()

plt.figure()
type_revenue.plot(kind="bar")
plt.title("Revenue per Transaction Type")
plt.savefig("revenue_type.png")
plt.close()

#final report
report = {"Total Transactions": len(df),
            "Total Revenue": df["Amount"].sum(),
            "Fraud Cases": df["Fraud"].sum(),
            "Average Transaction": df["Amount"].mean()}

report_df = pd.DataFrame([report])
report_df.to_csv("report.csv", index=False)

print("Report Successful!")