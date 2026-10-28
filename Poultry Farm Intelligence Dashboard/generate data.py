import numpy as np
import pandas as pd

#Generate data to be used
np.random.seed(42)

n = 10000

df = pd.DataFrame({
    "Farm_ID": np.random.randint(1000, 1100, n),
    "Age_Days": np.random.randint(1, 45, n),
    "Feed_Consumed_KG": np.random.normal(4, 1, n),
    "Weight_KG": np.random.normal(2.5, 0.5, n),
    "Mortality": np.random.choice([0,1], n, p=[0.95,0.05]),
    "Province": np.random.choice(
        ["Limpopo","Gauteng","Mpumalanga","KZN"],
        n
    )
})

# Create corrupt data
df.loc[50:100, "Feed_Consumed_KG"] = np.nan
df.loc[100:150, "Province"] = "limpopo"
df.loc[200:250, "Weight_KG"] = -5
df = pd.concat([df, df.iloc[0:50]])

# Save as CSV
df.to_csv("bank_dataset.csv", index=False)

print("CSV file created successfully!")