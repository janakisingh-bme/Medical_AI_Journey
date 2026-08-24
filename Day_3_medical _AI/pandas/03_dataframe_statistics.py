import pandas as pd

data = {
    "Marks": [80, 85, 75, 90, 70]
}

df = pd.DataFrame(data)

print("Mean:", df["Marks"].mean())
print("Maximum:", df["Marks"].max())
print("Minimum:", df["Marks"].min())