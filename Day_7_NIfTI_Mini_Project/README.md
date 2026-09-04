# 🧠 Day 7 — NIfTI Medical Image Analysis

A beginner-friendly Medical AI mini project focused on reading, analyzing, and visualizing **NIfTI (.nii / .nii.gz)** medical imaging files using Python and SimpleITK.

---

## 📌 Project Overview

NIfTI (Neuroimaging Informatics Technology Initiative) is a medical imaging file format commonly used in **neuroimaging and medical image analysis**.

In this project, I learned how to:

* Read NIfTI medical images using **SimpleITK**
* Understand 3D medical image dimensions
* Access voxel data
* Analyze basic image properties
* Extract and visualize 2D slices
* Display medical image data using **Matplotlib**
* Work with medical imaging data in Python

---

## 🛠️ Technologies Used

* 🐍 Python 3.12
* 🧠 SimpleITK
* 📊 NumPy
* 📈 Matplotlib
* 💻 VS Code
* 🔧 Git & GitHub

---

## 📂 Project Structure

```text
Day_7_NIfTI_Mini_Project/
│
├── data/
│   └── sample.nii.gz
│
├── outputs/
│   └── nifti_slices.png
│
├── nifti_analysis.py
│
└── README.md
```

---

## 🔬 What is NIfTI?

**NIfTI** stands for **Neuroimaging Informatics Technology Initiative**.

It is a file format designed to store medical imaging data, particularly images obtained from modalities such as:

* MRI
* fMRI
* CT
* PET

Unlike a typical 2D image, a NIfTI file can contain a **3D or 4D volume**.

For example:

```text
MRI Volume
     ↓
┌───────────────┐
│ Slice 1       │
│ Slice 2       │
│ Slice 3       │
│     ...       │
│ Slice N       │
└───────────────┘
```

---

## 🧊 Understanding Voxels

A **voxel** is the 3D equivalent of a pixel.

* Pixel → represents a point in a 2D image
* Voxel → represents a small volume in a 3D medical image

A NIfTI image can therefore be represented as a 3D array:

```text
Width × Height × Depth

Example:

128 × 128 × 64
```

This means the image contains:

```text
128 pixels × 128 pixels × 64 slices
```

---

## 📊 Image Analysis

The project examines important properties of the NIfTI image, such as:

* Image size
* Number of dimensions
* Voxel values
* Minimum voxel intensity
* Maximum voxel intensity
* Image spacing
* Image origin
* Image direction

These properties help understand how the medical image is stored and represented.

---

## 🖼️ Slice Visualization

A 3D medical image can be viewed one slice at a time.

```text
        3D NIfTI Volume
              │
              ▼
       ┌─────────────┐
       │   Volume    │
       └──────┬──────┘
              │
       ┌──────┼──────┐
       ▼      ▼      ▼
    Slice 1 Slice 2 Slice 3
       │      │      │
       ▼      ▼      ▼
     Image  Image  Image
```

This makes it easier to visually inspect different anatomical regions within the volume.

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Navigate to the project

```bash
cd Day_7_NIfTI_Mini_Project
```

### 3. Install dependencies

```bash
pip install SimpleITK numpy matplotlib
```

### 4. Run the analysis

```bash
python nifti_analysis.py
```

---

## 📚 Key Learnings

Through this project, I learned:

1. What NIfTI files are
2. Difference between pixels and voxels
3. How medical images can be stored as 3D volumes
4. How to read NIfTI files using SimpleITK
5. How to inspect image metadata
6. How to access voxel data
7. How to extract 2D slices from a 3D volume
8. How to visualize medical imaging data using Python

---

## 🎯 Medical AI Relevance

Understanding medical image formats is an important foundation for **Medical AI and Computer Vision**.

Before applying deep learning models to medical images, it is important to understand:

```text
Medical Image
      ↓
File Format
      ↓
Image Loading
      ↓
Voxel Data
      ↓
Preprocessing
      ↓
Visualization
      ↓
AI / Deep Learning Model
```

This project represents an early step toward working with **3D medical imaging and AI-based medical image analysis**.

---

## 🔮 Next Steps

Possible improvements for this project include:

* 3D volume visualization
* Image normalization
* Resampling medical images
* Image segmentation
* 3D visualization
* MRI preprocessing
* Introduction to medical image deep learning

---

## 👩‍💻 Author

**Janaki Singh**

Medical AI Learning Journey — Day 7

---

⭐ If you found this project useful, consider giving the repository a star!
