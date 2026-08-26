import pydicom
from pydicom import examples
import matplotlib.pyplot as plt

# Get sample CT DICOM file
path = examples.get_path("ct")

# Read DICOM file
ds = pydicom.dcmread(path)

# Extract pixel data
image = ds.pixel_array.astype(float)

# Apply windowing
window_level = 1000
window_width = 800

lower = window_level - window_width / 2
upper = window_level + window_width / 2

windowed_image = image.copy()
windowed_image[windowed_image < lower] = lower
windowed_image[windowed_image > upper] = upper

# Create comparison
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap="gray")
plt.title("Original CT")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(windowed_image, cmap="gray")
plt.title("Windowed CT")
plt.axis("off")

plt.show()