import wfdb
import numpy as np
import matplotlib.pyplot as plt

# Load ECG signal
record = wfdb.rdrecord("100", pn_dir="mitdb")

# Load annotations
annotation = wfdb.rdann("100", "atr", pn_dir="mitdb")

# Extract MLII signal
ecg_signal = record.p_signal[:, 0]

# Sampling frequency
fs = record.fs

# Number of samples before and after R-peak
before = 150
after = 180

# Store heartbeat segments
beats = []

# Extract beats around annotated locations
for r_peak in annotation.sample:

    start = r_peak - before
    end = r_peak + after

    # Make sure segment is inside signal boundaries
    if start >= 0 and end < len(ecg_signal):

        beat = ecg_signal[start:end]
        beats.append(beat)

beats = np.array(beats)

# Display information
print("ECG Beat Segmentation")
print("=====================")
print("Sampling Frequency:", fs, "Hz")
print("Total ECG Samples:", len(ecg_signal))
print("Total Annotations:", len(annotation.sample))
print("Extracted Beats:", len(beats))
print("Samples per Beat:", beats.shape[1])

# Plot first 5 heartbeat segments
plt.figure(figsize=(12, 6))

for i in range(5):
    plt.plot(beats[i], label=f"Beat {i + 1}")

plt.title("First 5 Segmented ECG Beats")
plt.xlabel("Sample")
plt.ylabel("Amplitude (mV)")
plt.legend()
plt.grid()

plt.show()