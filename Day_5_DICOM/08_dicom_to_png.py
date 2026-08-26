import pydicom
from pydicom import examples
import matplotlib.pyplot as plt

# Get sample CT DICOM file
path = examples.get_path("ct")

# Read DICOM file
ds = pydicom.dcmread(path)

# Extract pixel data
image = ds.pixel_array

# Save image as PNG
plt.imsave("ct_image.png", image, cmap="gray")

print("DICOM image successfully saved as ct_image.png")