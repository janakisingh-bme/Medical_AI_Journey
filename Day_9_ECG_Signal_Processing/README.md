# 🫀 Day 9 — ECG Signal Processing

A practical introduction to **ECG signal processing using Python**, developed as part of my Medical AI learning journey.

This project uses a real ECG recording from the **MIT-BIH Arrhythmia Database** and demonstrates the complete process of loading, analyzing, filtering, segmenting, labeling, and preparing ECG heartbeats for future machine learning applications.

---

## 🎯 Objectives

The main objectives of this project are:

- Load real ECG signals using WFDB
- Understand ECG sampling frequency and signal dimensions
- Visualize ECG waveforms
- Calculate ECG signal statistics
- Normalize ECG signals
- Apply band-pass filtering
- Segment individual heartbeats
- Extract ECG annotation labels
- Analyze class distribution
- Visualize different ECG beat classes
- Save ECG beats and labels as reusable NumPy datasets
- Prepare the foundation for future ECG machine learning and 1D-CNN classification

---

## 🛠️ Technologies Used

- **Python 3**
- **NumPy** — numerical and array operations
- **Matplotlib** — ECG visualization
- **SciPy** — digital signal filtering
- **WFDB** — ECG database and annotation handling

---

## 📂 Project Structure

```text
Day_9_ECG_Signal_Processing/
│
├── data/
│
├── outputs/
│   ├── ecg_beats.npy
│   └── ecg_labels.npy
│
├── 01_load_ecg.py
├── 02_plot_ecg.py
├── 03_ecg_statistics.py
├── 04_normalize_ecg.py
├── 05_filter_ecg.py
├── 06_compare_signals.py
├── 07_ecg_segmentation.py
├── 08_ecg_labels.py
├── 09_prepare_ecg_dataset.py
├── 10_visualize_ecg_classes.py
├── 11_save_ecg_dataset.py
└── README.md

The next stage of the Medical AI journey will focus on building a more suitable ECG machine-learning dataset.

Planned steps include:

Use multiple MIT-BIH records
Increase the number of abnormal beats
Handle class imbalance
Build training and testing datasets
Encode ECG labels
Apply preprocessing consistently
Train a baseline machine-learning model
Prepare ECG data for a future 1D-CNN classifier