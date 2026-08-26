import pydicom
from pydicom import examples
import cv2
import matplotlib.pyplot as plt

# Get sample CT DICOM file
path = examples.get_path("ct")

# Read DICOM file
ds = pydicom.dcmread(path)

# Extract pixel data
image = ds.pixel_array

# Normalize pixel values to 0-255
normalized = cv2.normalize(
    image, None, 0, 255, cv2.NORM_MINMAX
).astype("uint8")

# Apply Gaussian blur
blurred = cv2.GaussianBlur(normalized, (5, 5), 0)

# Display original and blurred images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(normalized, cmap="gray")
plt.title("Original CT")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(blurred, cmap="gray")
plt.title("Blurred CT")
plt.axis("off")

plt.show()