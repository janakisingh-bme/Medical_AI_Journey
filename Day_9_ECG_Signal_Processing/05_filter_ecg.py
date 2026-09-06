import wfdb
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

# Load ECG record
record = wfdb.rdrecord("100", pn_dir="mitdb")

# Extract MLII signal
ecg_signal = record.p_signal[:, 0]

# Sampling frequency
fs = record.fs

# Create band-pass filter
low_cutoff = 0.5
high_cutoff = 40

nyquist = fs / 2

low = low_cutoff / nyquist
high = high_cutoff / nyquist

b, a = butter(4, [low, high], btype="band")

# Apply filter
filtered_ecg = filtfilt(b, a, ecg_signal)

# Plot first 10 seconds
samples = int(10 * fs)
time = np.arange(samples) / fs

plt.figure(figsize=(12, 5))

plt.plot(time, ecg_signal[:samples], label="Original ECG")
plt.plot(time, filtered_ecg[:samples], label="Filtered ECG")

plt.title("Original vs Filtered ECG - Record 100 (MLII)")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude (mV)")
plt.legend()
plt.grid()

plt.show()