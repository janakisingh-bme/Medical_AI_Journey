import wfdb
from collections import Counter

# Load annotations
annotation = wfdb.rdann("100", "atr", pn_dir="mitdb")

# Get annotation symbols
symbols = annotation.symbol

# Count each type
label_counts = Counter(symbols)

print("ECG Annotation Labels")
print("=====================")

for label, count in label_counts.items():
    print(f"{label}: {count}")