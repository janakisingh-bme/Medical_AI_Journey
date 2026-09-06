import wfdb
import matplotlib.pyplot as plt

# Load ECG record
record = wfdb.rdrecord("100", pn_dir="mitdb")

# Extract ECG signal
ecg_signal = record.p_signal[:, 0]

# Sampling frequency
fs = record.fs

# Plot first 10 seconds
samples = int(10 * fs)

time = [i / fs for i in range(samples)]

plt.figure(figsize=(12, 4))
plt.plot(time, ecg_signal[:samples])

plt.title("ECG Signal - Record 100 (MLII)")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude (mV)")
plt.grid()

plt.savefig("outputs/ecg_raw_10s.png", dpi=300, bbox_inches="tight")
plt.show()