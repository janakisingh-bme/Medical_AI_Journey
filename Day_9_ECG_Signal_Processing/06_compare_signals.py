import wfdb
import numpy as np
from scipy.signal import butter, filtfilt

# Load ECG record
record = wfdb.rdrecord("100", pn_dir="mitdb")

# Extract MLII
ecg_signal = record.p_signal[:, 0]

# Sampling frequency
fs = record.fs

# -----------------------------
# Band-pass filtering
# -----------------------------

low_cutoff = 0.5
high_cutoff = 40

nyquist = fs / 2

low = low_cutoff / nyquist
high = high_cutoff / nyquist

b, a = butter(4, [low, high], btype="band")

filtered_ecg = filtfilt(b, a, ecg_signal)

# -----------------------------
# Normalization
# -----------------------------

normalized_ecg = (
    (filtered_ecg - np.mean(filtered_ecg))
    / np.std(filtered_ecg)
)

# -----------------------------
# Print comparison
# -----------------------------

print("ECG Signal Comparison")
print("=====================")

print("\nOriginal ECG")
print("Mean:", np.mean(ecg_signal))
print("Std:", np.std(ecg_signal))
print("Min:", np.min(ecg_signal))
print("Max:", np.max(ecg_signal))

print("\nFiltered ECG")
print("Mean:", np.mean(filtered_ecg))
print("Std:", np.std(filtered_ecg))
print("Min:", np.min(filtered_ecg))
print("Max:", np.max(filtered_ecg))

print("\nFiltered + Normalized ECG")
print("Mean:", np.mean(normalized_ecg))
print("Std:", np.std(normalized_ecg))
print("Min:", np.min(normalized_ecg))
print("Max:", np.max(normalized_ecg))