import pydicom
from pydicom import examples
import numpy as np
import matplotlib.pyplot as plt
import cv2


def load_dicom():
    """Load the sample CT DICOM file."""
    path = examples.get_path("ct")
    ds = pydicom.dcmread(path)
    return ds


def display_metadata(ds):
    """Display important DICOM metadata."""
    print("\n========== DICOM INFORMATION ==========")
    print("Patient Name :", ds.get("PatientName", "Not available"))
    print("Patient ID   :", ds.get("PatientID", "Not available"))
    print("Modality     :", ds.get("Modality", "Not available"))
    print("Study Date   :", ds.get("StudyDate", "Not available"))
    print("Rows         :", ds.get("Rows", "Not available"))
    print("Columns      :", ds.get("Columns", "Not available"))
    print("========================================")


def analyze_pixels(ds):
    """Analyze the DICOM pixel data."""
    image = ds.pixel_array

    print("\n========== PIXEL ANALYSIS ==========")
    print("Image shape       :", image.shape)
    print("Number of pixels  :", image.size)
    print("Data type         :", image.dtype)
    print("Minimum value     :", image.min())
    print("Maximum value     :", image.max())
    print("====================================")


def calculate_statistics(ds):
    """Calculate basic statistics of the DICOM image."""
    image = ds.pixel_array.astype(float)

    print("\n========== IMAGE STATISTICS ==========")
    print("Mean pixel value      :", np.mean(image))
    print("Standard deviation    :", np.std(image))
    print("Minimum pixel value   :", np.min(image))
    print("Maximum pixel value   :", np.max(image))
    print("=======================================")


def apply_windowing(ds):
    """Apply CT windowing to the image."""
    image = ds.pixel_array.astype(float)

    window_level = 1000
    window_width = 800

    lower = window_level - window_width / 2
    upper = window_level + window_width / 2

    windowed_image = np.clip(image, lower, upper)

    return image, windowed_image


def normalize_image(image):
    """Normalize image values to 0-255."""
    normalized = cv2.normalize(
        image,
        None,
        0,
        255,
        cv2.NORM_MINMAX
    )

    return normalized.astype(np.uint8)


def apply_opencv_processing(image):
    """Apply Gaussian blur and Canny edge detection."""
    blurred = cv2.GaussianBlur(
        image,
        (5, 5),
        0
    )

    edges = cv2.Canny(
        blurred,
        50,
        150
    )

    return blurred, edges


def display_results(original, windowed, normalized, blurred, edges):
    """Display all image-processing results."""

    plt.figure(figsize=(15, 8))

    plt.subplot(2, 3, 1)
    plt.imshow(original, cmap="gray")
    plt.title("Original CT")
    plt.axis("off")

    plt.subplot(2, 3, 2)
    plt.imshow(windowed, cmap="gray")
    plt.title("Windowed CT")
    plt.axis("off")

    plt.subplot(2, 3, 3)
    plt.imshow(normalized, cmap="gray")
    plt.title("Normalized")
    plt.axis("off")

    plt.subplot(2, 3, 4)
    plt.imshow(blurred, cmap="gray")
    plt.title("Gaussian Blur")
    plt.axis("off")

    plt.subplot(2, 3, 5)
    plt.imshow(edges, cmap="gray")
    plt.title("Canny Edges")
    plt.axis("off")

    plt.tight_layout()
    plt.show()


def main():
    print("========================================")
    print("   MEDICAL DICOM ANALYSIS TOOLKIT")
    print("========================================")

    # Load DICOM
    ds = load_dicom()

    print("\nDICOM file loaded successfully!")

    # DICOM analysis
    display_metadata(ds)
    analyze_pixels(ds)
    calculate_statistics(ds)

    # Windowing
    original, windowed = apply_windowing(ds)

    # OpenCV processing
    normalized = normalize_image(windowed)
    blurred, edges = apply_opencv_processing(normalized)

    # Display results
    display_results(
        original,
        windowed,
        normalized,
        blurred,
        edges
    )


if __name__ == "__main__":
    main()