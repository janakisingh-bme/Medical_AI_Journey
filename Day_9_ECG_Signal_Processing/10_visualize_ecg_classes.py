import wfdb
import numpy as np
import matplotlib.pyplot as plt

# Load ECG record
record = wfdb.rdrecord("100", pn_dir="mitdb")
annotation = wfdb.rdann("100", "atr", pn_dir="mitdb")

# Extract MLII
ecg_signal = record.p_signal[:, 0]

# Segmentation parameters
before = 150
after = 180

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

        beats.append(ecg_signal[start:end])
        labels.append(symbol)

beats = np.array(beats)
labels = np.array(labels)

# Find one example of each class
normal_index = np.where(labels == "N")[0][0]
atrial_index = np.where(labels == "A")[0][0]
ventricular_index = np.where(labels == "V")[0][0]

# Plot
plt.figure(figsize=(12, 6))

plt.plot(
    beats[normal_index],
    label="Normal (N)"
)

plt.plot(
    beats[atrial_index],
    label="Atrial Premature (A)"
)

plt.plot(
    beats[ventricular_index],
    label="Ventricular Premature (V)"
)

plt.axvline(
    x=before,
    linestyle="--",
    label="R-peak"
)

plt.title("Comparison of ECG Beat Classes")
plt.xlabel("Sample")
plt.ylabel("Amplitude (mV)")
plt.legend()
plt.grid()

plt.savefig("outputs/ecg_beat_classes.png", dpi=300, bbox_inches="tight")
plt.show()