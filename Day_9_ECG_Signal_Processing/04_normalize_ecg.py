import wfdb
import numpy as np
import matplotlib.pyplot as plt

# Load ECG record
record = wfdb.rdrecord("100", pn_dir="mitdb")

# Extract MLII signal
ecg_signal = record.p_signal[:, 0]

# Calculate mean and standard deviation
mean = np.mean(ecg_signal)
std = np.std(ecg_signal)

# Z-score normalization
normalized_ecg = (ecg_signal - mean) / std

# Print statistics
print("Original ECG")
print("Mean:", np.mean(ecg_signal))
print("Standard Deviation:", np.std(ecg_signal))

print("\nNormalized ECG")
print("Mean:", np.mean(normalized_ecg))
print("Standard Deviation:", np.std(normalized_ecg))

# Plot first 10 seconds
samples = int(10 * record.fs)
time = np.arange(samples) / record.fs

plt.figure(figsize=(12, 4))
plt.plot(time, normalized_ecg[:samples])

plt.title("Normalized ECG Signal - Record 100 (MLII)")
plt.xlabel("Time (seconds)")
plt.ylabel("Normalized Amplitude")
plt.grid()
plt.savefig("outputs/ecg_normalized_10s.png", dpi=300, bbox_inches="tight")
plt.show()