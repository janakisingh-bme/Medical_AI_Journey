import pydicom
from pydicom import examples
import numpy as np

# Get sample CT DICOM file
path = examples.get_path("ct")

# Read DICOM file
ds = pydicom.dcmread(path)

# Extract pixel data
image = ds.pixel_array

# Calculate image statistics
print("Image Statistics")
print("----------------")
print("Mean pixel value:", np.mean(image))
print("Standard deviation:", np.std(image))
print("Minimum pixel value:", np.min(image))
print("Maximum pixel value:", np.max(image))