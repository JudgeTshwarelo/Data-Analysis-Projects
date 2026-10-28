#Poultry Farm Intelligence Dashboard

#Goal - Analyze a commercial poultry farm with 10,000+ production records.

#Skills
    #NumPy
    #Pandas
    #Matplotlib

import pandas as pd
import matplotlib.pyplot as plt

#Tasks
#Level 1 - Clean Data
df = pd.read_csv("poultry_dataset.csv")

df = df.drop_duplicates()   #   Remove duplicates

df["Province"] = df["Province"].replace({"limpopo": "Limpopo",      #   Fix province names
                                         "Gauteng": "GAUTENG",
                                         "KZN": "KWA-ZULU NATAL",
                                         "Mpumalanga": "MPUMALANGA"
                                         })

df = df.fillna({"Feed_Consumed_KG": 0}) #   Fill missing values

df = df[df["Weight_KG"] >= 0]   #   Remove negative weights

#Level 2 - Farm Analytics
#Calculate:

group = df.groupby("Province")  #Per province.

#print(group["Weight_KG"].mean())    #   Average Weight
#print(group["Feed_Consumed_KG"].mean()) #   Average Feed
#print(group["Mortality"].sum()) #   Mortality Rate
#print(group["Province"].count())    #   Total Birds

#Level 3 - Visualizations
#Create:

#1 Mortality by Province
mortality_by_province = df.groupby("Province")["Mortality"].sum()

x_label = mortality_by_province.index
y_label = mortality_by_province.values

plt.bar(x_label, y_label,   #   Bar Chart
        color="blue",
        edgecolor="yellow")

plt.title("Mortality by Province", fontsize=29,
          family="Arial",
          fontweight="bold",
          color="Blue")

plt.xlabel("Province", fontsize=20,
          family="Arial",
          fontweight="bold",
          color="Blue")

plt.ylabel("Mortality", fontsize=20,
          family="Arial",
          fontweight="bold",
          color="Blue")

plt.tight_layout()
plt.show()

#2 Feed vs Weight
#   Scatter Plot

'''plt.scatter(df["Feed_Consumed_KG"], df["Weight_KG"],
            color="Blue",
            alpha=0.7,
            s=100)

plt.title("Feed consumption vs Weight", fontsize=29,
          family="Arial",
          fontweight="bold",
          color="Blue")
plt.xlabel("Feed Consumed (KG)", fontsize=20,
          family="Arial",
          fontweight="bold",
          color="red")
plt.ylabel("Weight (KG)", fontsize=20,
          family="Arial",
          fontweight="bold",
          color="green")

plt.tight_layout()
plt.legend()
plt.show()'''

#Level 4 - Advanced
#Detect farms with:
#   Mortality > 10%
#Flag them.

#Create:
#   High Risk Farms Report

#GitHub Repo-Name - "Poultry-Farm-Analytics-Dashboard"
#This would impress agricultural companies.