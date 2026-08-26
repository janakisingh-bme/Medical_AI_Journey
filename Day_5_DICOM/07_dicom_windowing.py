import pydicom
from pydicom import examples
import matplotlib.pyplot as plt

# Get sample CT DICOM file
path = examples.get_path("ct")

# Read DICOM file
ds = pydicom.dcmread(path)

# Extract pixel data
image = ds.pixel_array.astype(float)

# Set window level and window width
window_level = 1000
window_width = 800

# Calculate window limits
lower = window_level - window_width / 2
upper = window_level + window_width / 2

# Apply windowing
windowed_image = image.copy()
windowed_image[windowed_image < lower] = lower
windowed_image[windowed_image > upper] = upper

# Display windowed image
plt.imshow(windowed_image, cmap="gray")
plt.title("Windowed CT Image")
plt.axis("off")
plt.show()