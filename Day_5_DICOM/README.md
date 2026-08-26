# Day 5 — DICOM & pydicom

## 📌 Overview

Today I learned the basics of **DICOM (Digital Imaging and Communications in Medicine)** and how to work with DICOM medical images using Python and the `pydicom` library.

I worked with a sample CT DICOM image and learned how to read its metadata, extract pixel data, visualize the image, perform basic processing, and convert it to PNG.

## 🎯 Objectives

* Understand what DICOM is
* Learn how to use `pydicom`
* Read DICOM files
* Extract DICOM metadata and tags
* Access medical image pixel data
* Display CT images using Matplotlib
* Calculate image statistics
* Understand CT image windowing
* Convert DICOM images to PNG
* Apply basic image processing using OpenCV

## 🛠️ Programs Completed

| File                     | What I Learned                                          |
| ------------------------ | ------------------------------------------------------- |
| `01_read_dicom.py`       | Read and display a complete DICOM dataset               |
| `02_dicom_metadata.py`   | Extract important DICOM metadata                        |
| `03_display_dicom.py`    | Display a CT DICOM image                                |
| `04_dicom_tags.py`       | Access individual DICOM tags                            |
| `05_pixel_data.py`       | Analyze pixel data, shape, range, and data type         |
| `06_image_statistics.py` | Calculate mean, standard deviation, minimum and maximum |
| `07_dicom_windowing.py`  | Apply CT image windowing                                |
| `08_dicom_to_png.py`     | Convert DICOM image data to PNG                         |
| `09_compare_images.py`   | Compare original and windowed CT images                 |
| `10_dicom_processing.py` | Apply basic OpenCV processing to DICOM data             |

## 🧠 Key Concepts

### DICOM

DICOM is a medical imaging standard that stores both:

* Medical image data
* Medical imaging metadata

### pydicom

`pydicom` is a Python library used to read and work with DICOM files.

### Pixel Data

DICOM pixel data can be extracted using:

```python
image = ds.pixel_array
```

The sample CT image used in this practice had:

* Image shape: `128 × 128`
* Minimum pixel value: `128`
* Maximum pixel value: `2191`
* Data type: `int16`

### Image Statistics

For the sample CT image:

* Mean pixel value: approximately `904.93`
* Standard deviation: approximately `379.76`

### CT Windowing

Windowing allows a selected intensity range of a CT image to be emphasized for visualization.

### Medical AI Pipeline

```text
DICOM File
    ↓
pydicom
    ↓
Metadata + Pixel Data
    ↓
NumPy Array
    ↓
Image Processing
    ↓
Medical AI
```

## 📁 Project Structure

```text
Day_5_DICOM/
│
├── data/
├── 01_read_dicom.py
├── 02_dicom_metadata.py
├── 03_display_dicom.py
├── 04_dicom_tags.py
├── 05_pixel_data.py
├── 06_image_statistics.py
├── 07_dicom_windowing.py
├── 08_dicom_to_png.py
├── 09_compare_images.py
├── 10_dicom_processing.py
├── ct_image.png
└── README.md
```

## 📚 Libraries Used

* Python
* pydicom
* NumPy
* Matplotlib
* OpenCV

## ✅ Day 5 Status

**Completed successfully.**

I can now read a DICOM file, extract its metadata and pixel data, visualize the CT image, analyze its pixel values, apply windowing, and perform basic image processing.


