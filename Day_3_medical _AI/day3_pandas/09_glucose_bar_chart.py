import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("patients.csv")

plt.bar(data["Name"], data["Glucose"])

plt.xlabel("Patient Name")
plt.ylabel("Glucose Level")
plt.title("Patient Glucose Levels")

plt.show()