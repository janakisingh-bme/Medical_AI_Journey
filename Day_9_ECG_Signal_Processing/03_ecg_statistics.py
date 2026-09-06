import wfdb
import numpy as np

# Load ECG record
record = wfdb.rdrecord("100", pn_dir="mitdb")

# Extract MLII signal
ecg_signal = record.p_signal[:, 0]

# Calculate statistics
mean_value = np.mean(ecg_signal)
std_value = np.std(ecg_signal)
min_value = np.min(ecg_signal)
max_value = np.max(ecg_signal)

print("ECG Signal Statistics")
print("----------------------")
print("Sampling Frequency:", record.fs, "Hz")
print("Number of Samples:", len(ecg_signal))
print("Mean Amplitude:", mean_value, "mV")
print("Standard Deviation:", std_value, "mV")
print("Minimum Amplitude:", min_value, "mV")
print("Maximum Amplitude:", max_value, "mV")