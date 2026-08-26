import pydicom
from pydicom import examples

# Get sample CT DICOM file
path = examples.get_path("ct")

# Read DICOM file
ds = pydicom.dcmread(path)

# Extract pixel data
image = ds.pixel_array

# Display information about the image
print("Pixel Data Information")
print("----------------------")
print("Image shape:", image.shape)
print("Minimum pixel value:", image.min())
print("Maximum pixel value:", image.max())
print("Data type:", image.dtype)