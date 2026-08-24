import pandas as pd

data = pd.read_csv("patients.csv")

print("Mean Glucose:", data["Glucose"].mean())
print("Maximum Glucose:", data["Glucose"].max())
print("Minimum Glucose:", data["Glucose"].min())