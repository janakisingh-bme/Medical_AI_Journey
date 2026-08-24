import pandas as pd

data = pd.read_csv("patients.csv")

high_glucose = data[data["Glucose"] > 120]

print(high_glucose)