#Generate Dataset
import numpy as np
import pandas as pd

np.random.seed(42)

n = 50000

df = pd.DataFrame({
    "Transaction_ID": range(n),
    "Customer_ID": np.random.randint(1000,5000,n),
    "Amount": np.random.exponential(1500,n),
    "Transaction_Type":
        np.random.choice(
            ["Deposit","Withdrawal","Transfer"],
            n
        ),
    "Province":
        np.random.choice(
            ["Limpopo","Gauteng","KZN"],
            n
        ),
    "Fraud":
        np.random.choice(
            [0,1],
            n,
            p=[0.98,0.02]
        )
})

#Corrupt Data
df.loc[100:500,"Amount"] = np.nan
df.loc[600:650,"Province"] = "lim"
df.loc[700:750,"Amount"] = -1000
df = pd.concat([df,df.iloc[0:100]])

df.to_csv("bank_dataset.csv", index=False)
print("CSV file created successfully!")