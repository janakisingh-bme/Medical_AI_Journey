import pandas as pd

data = {
    "Name": ["A", "B", "C", "D", "E", "F"],
    "Marks": [70, 80, 90, 85, 75, 88]
}

df = pd.DataFrame(data)

print("First five records:")
print(df.head())

print("Last five records:")
print(df.tail())