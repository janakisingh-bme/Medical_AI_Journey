import pandas as pd

data = {
    "Name": ["Ram", "Sita", "Hari"],
    "Age": [20, 21, 19],
    "Marks": [80, 85, 75]
}

df = pd.DataFrame(data)

print(df[df["Marks"] > 80])