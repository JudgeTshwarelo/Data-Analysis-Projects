"""
Level 1: Beginner Analyst Project (Student Marks Analyzer)
This teaches the basics of Pandas and visualization.

Skills
1. Reading CSV
2. Cleaning data
3. Calculating statistics
4, Visualization"""

#Tasks
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students.csv")    #-Load the data

#-Basic Analysis
df["Total"] = df["Math"] + df["Physics"] + df["Programming"]
top_students = df.sort_values(by="Total", ascending=True)   #    Top student

#-Visualization
df.set_index("Name")[["Math", "Physics","Programming"]].plot(kind="bar")
plt.title("Student Performance")    #Title
plt.ylabel("Marks")
plt.xlabel("Names")

plt.show()
