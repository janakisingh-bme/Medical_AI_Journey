import wfdb
import numpy as np
from collections import Counter

# Load ECG record
record = wfdb.rdrecord("100", pn_dir="mitdb")
annotation = wfdb.rdann("100", "atr", pn_dir="mitdb")

# Extract MLII signal
ecg_signal = record.p_signal[:, 0]

# Sampling frequency
fs = record.fs

# Segmentation window
before = 150
after = 180

# Beat classes we want
valid_labels = ["N", "A", "V"]

beats = []
labels = []

# Extract labeled beats
for sample, symbol in zip(annotation.sample, annotation.symbol):

    # Ignore non-beat annotations
    if symbol not in valid_labels:
        continue

    start = sample - before
    end = sample + after

    # Check boundaries
    if start >= 0 and end < len(ecg_signal):

        beat = ecg_signal[start:end]

        beats.append(beat)
        labels.append(symbol)

# Convert to NumPy arrays
beats = np.array(beats)
labels = np.array(labels)

# Display dataset information
print("ECG Dataset")
print("===========")

print("Total beats:", len(beats))
print("Beat shape:", beats.shape)

print("\nClass distribution:")
class_counts = Counter(labels)

for label, count in class_counts.items():
    print(f"{label}: {count}")

print("\nUnique labels:", np.unique(labels))