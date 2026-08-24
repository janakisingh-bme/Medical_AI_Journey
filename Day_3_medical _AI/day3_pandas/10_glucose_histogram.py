import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("patients.csv")

plt.hist(data["Glucose"])

plt.xlabel("Glucose Level")
plt.ylabel("Number of Patients")
plt.title("Distribution of Glucose Levels")

plt.show()