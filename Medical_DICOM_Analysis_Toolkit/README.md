# Medical DICOM Analysis Toolkit

A beginner-friendly **Medical Image Processing project** developed using Python to analyze and process CT DICOM images.

This project combines **PyDICOM, NumPy, OpenCV, and Matplotlib** to demonstrate a basic medical image analysis workflow.

---

## 📌 Project Overview

DICOM (Digital Imaging and Communications in Medicine) is a standard format used for storing and exchanging medical images along with patient and examination information.

This project loads a sample CT DICOM image and performs:

* DICOM metadata extraction
* Pixel data analysis
* Statistical analysis
* CT windowing
* Image normalization
* Gaussian blur
* Canny edge detection
* Visualization of processed images

The project is designed as part of a **Medical AI / Medical Image Processing learning journey**.

---

## 🛠️ Technologies Used

| Technology | Purpose                            |
| ---------- | ---------------------------------- |
| Python     | Main programming language          |
| PyDICOM    | Reading and processing DICOM files |
| NumPy      | Numerical and pixel-data analysis  |
| OpenCV     | Image processing                   |
| Matplotlib | Image visualization                |

---

## 📂 Project Structure

```text
Medical_AI_Journey/
│
├── DICOM_Analysis/
│   └── dicom_analysis_toolkit.py
│
├── README.md
│
└── requirements.txt
```

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/janakisingh-bme/Medical_AI_Journey.git
```

### 2. Open the project

```bash
cd Medical_AI_Journey
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

On Windows:

```bash
venv\Scripts\activate
```

### 5. Install required libraries

```bash
pip install pydicom numpy matplotlib opencv-python
```

---

## ▶️ How to Run

Run the Python program:

```bash
python dicom_analysis_toolkit.py
```

The program loads the sample CT DICOM file provided by PyDICOM and displays the analysis results.

---

## 🔬 Project Workflow

```text
        DICOM CT File
              │
              ▼
       Load DICOM using
           PyDICOM
              │
              ▼
      Extract Metadata
              │
              ▼
       Extract Pixel Data
              │
              ▼
      Pixel Analysis
              │
              ▼
    Statistical Analysis
              │
              ▼
       CT Windowing
              │
              ▼
      Normalize Image
              │
              ▼
       Gaussian Blur
              │
              ▼
      Canny Edge Detection
              │
              ▼
       Display Results
```

---

## 🩻 1. Loading the DICOM File

The project uses PyDICOM's sample CT image:

```python
path = examples.get_path("ct")
ds = pydicom.dcmread(path)
```

The DICOM dataset contains both:

* Medical image data
* Metadata about the examination

---

## 📋 2. DICOM Metadata Analysis

The program extracts important information such as:

```text
Patient Name
Patient ID
Modality
Study Date
Rows
Columns
```

Example:

```python
print("Patient Name :", ds.get("PatientName", "Not available"))
print("Modality     :", ds.get("Modality", "Not available"))
```

The `get()` method is used so the program does not crash if a particular DICOM attribute is unavailable.

---

## 🧮 3. Pixel Data Analysis

The actual image is accessed using:

```python
image = ds.pixel_array
```

The program analyzes:

* Image shape
* Number of pixels
* Data type
* Minimum pixel value
* Maximum pixel value

Example:

```text
Image shape      : (128, 128)
Number of pixels : 16384
Data type        : int16
```

The exact values depend on the DICOM image being analyzed.

---

## 📊 4. Image Statistics

NumPy is used to calculate basic statistical properties:

```python
np.mean(image)
np.std(image)
np.min(image)
np.max(image)
```

These values provide information about the distribution and intensity of pixels in the image.

### Statistics calculated

* **Mean** → Average pixel intensity
* **Standard deviation** → Variation in pixel intensity
* **Minimum** → Lowest pixel value
* **Maximum** → Highest pixel value

---

## 🎚️ 5. CT Windowing

CT windowing is applied to highlight a selected range of image intensities.

The project uses:

```python
window_level = 1000
window_width = 800
```

The lower and upper limits are calculated as:

```python
lower = window_level - window_width / 2
upper = window_level + window_width / 2
```

Then the pixel values are clipped:

```python
windowed_image = np.clip(image, lower, upper)
```

This helps emphasize a particular range of intensities.

---

## 🔄 6. Image Normalization

OpenCV is used to convert the windowed image into the range **0–255**:

```python
cv2.normalize(
    image,
    None,
    0,
    255,
    cv2.NORM_MINMAX
)
```

The result is converted to:

```python
np.uint8
```

This makes the image suitable for standard image-processing operations.

---

## 🌫️ 7. Gaussian Blur

Gaussian filtering is applied to reduce noise:

```python
blurred = cv2.GaussianBlur(
    image,
    (5, 5),
    0
)
```

The `(5, 5)` kernel is used for smoothing.

Gaussian blur can help reduce small variations before performing edge detection.

---

## 🔲 8. Canny Edge Detection

The project uses OpenCV's Canny algorithm:

```python
edges = cv2.Canny(
    blurred,
    50,
    150
)
```

Canny edge detection identifies strong intensity changes in the image.

This can help highlight structures and boundaries within medical images.

---

## 🖼️ 9. Visualization

Matplotlib displays five stages of processing:

1. Original CT
2. Windowed CT
3. Normalized image
4. Gaussian-blurred image
5. Canny edge image

The images are displayed using:

```python
plt.imshow(image, cmap="gray")
```

The grayscale color map is appropriate for displaying CT images.

---

## 📸 Output

The final visualization contains:

```text
┌─────────────────┬─────────────────┬─────────────────┐
│   Original CT   │   Windowed CT   │    Normalized   │
├─────────────────┼─────────────────┼─────────────────┤
│  Gaussian Blur  │  Canny Edges    │                 │
└─────────────────┴─────────────────┴─────────────────┘
```

The program also prints DICOM metadata, pixel information, and image statistics in the terminal.

---

## 🧠 Concepts Learned

This project demonstrates several important concepts in medical image processing:

* DICOM file handling
* Medical image metadata
* Pixel arrays
* NumPy numerical operations
* Image statistics
* CT windowing
* Image normalization
* Gaussian filtering
* Edge detection
* Medical image visualization
* Python functions and modular programming

---

## ⚠️ Important Note

This project is an **educational medical image-processing project**.

The image-processing results are not intended for clinical diagnosis or medical decision-making.

The current version uses a PyDICOM sample CT image and does **not** perform clinical diagnosis.

---

## 🚀 Future Improvements

Planned improvements include:

* Support for user-provided DICOM files
* Hounsfield Unit conversion
* Lung, brain, and bone CT windows
* Histogram analysis
* Thresholding
* Morphological operations
* Contour detection
* Region of Interest (ROI) analysis
* Image segmentation
* Saving processed images
* Automated analysis reports
* Multiple DICOM slice handling
* 3D CT visualization
* Machine learning-based medical image classification

---

## 👩‍💻 Author

**Janaki Singh**

Medical AI Learning Journey
Electronics, Communication and Automation (ECA)

---

## ⭐ Learning Goal

The goal of this project is to gradually build practical skills in:

```text
Python
   ↓
NumPy
   ↓
Matplotlib
   ↓
OpenCV
   ↓
DICOM
   ↓
Medical Image Processing
   ↓
Medical AI
```

This project represents the transition from basic Python/image-processing exercises toward practical **Medical AI applications**.
