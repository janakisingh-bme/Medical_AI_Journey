import wfdb

# Load ECG record
record = wfdb.rdrecord("100", pn_dir="mitdb")

# Display basic information
print("ECG Record Loaded Successfully!")
print("Sampling Frequency:", record.fs)
print("Number of Samples:", record.sig_len)
print("Number of Signals:", record.n_sig)
print("Signal Names:", record.sig_name)