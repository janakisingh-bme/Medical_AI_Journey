import wfdb
import numpy as np
import os

# Load ECG record
record = wfdb.rdrecord("100", pn_dir="mitdb")
annotation = wfdb.rdann("100", "atr", pn_dir="mitdb")

# Extract MLII
ecg_signal = record.p_signal[:, 0]

# Segmentation parameters
before = 150
after = 180

# Classes
valid_labels = ["N", "A", "V"]

beats = []
labels = []

# Extract labeled beats
for sample, symbol in zip(annotation.sample, annotation.symbol):

    if symbol not in valid_labels:
        continue

    start = sample - before
    end = sample + after

    if start >= 0 and end < len(ecg_signal):

        beat = ecg_signal[start:end]

        beats.append(beat)
        labels.append(symbol)

# Convert to NumPy arrays
beats = np.array(beats)
labels = np.array(labels)

# Create output directory
os.makedirs("outputs", exist_ok=True)

# Save dataset
np.save("outputs/ecg_beats.npy", beats)
np.save("outputs/ecg_labels.npy", labels)

print("ECG dataset saved successfully!")
print("-----------------------------")
print("Beats shape:", beats.shape)
print("Labels shape:", labels.shape)
print("Saved files:")
print("outputs/ecg_beats.npy")
print("outputs/ecg_labels.npy")