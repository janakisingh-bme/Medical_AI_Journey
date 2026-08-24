import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("patients.csv")

print("Average Glucose:", data["Glucose"].mean())

high_glucose = data[data["Glucose"] > 120]

print("\nPatients with High Glucose:")
print(high_glucose)

plt.bar(data["Name"], data["Glucose"])

plt.xlabel("Patient Name")
plt.ylabel("Glucose Level")
plt.title("Patient Glucose Analysis")

plt.show()