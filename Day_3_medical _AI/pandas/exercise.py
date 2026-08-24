import pandas as pd

data = {
    "Patient": ["A", "B", "C", "D"],
    "Age": [25, 30, 35, 28],
    "Heart_Rate": [75, 110, 85, 120]
}

df = pd.DataFrame(data)

print("Patient Data:")
print(df)

print("\nPatients with heart rate above 100:")
print(df[df["Heart_Rate"] > 100])