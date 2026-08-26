import pydicom
from pydicom import examples
import matplotlib.pyplot as plt

# Get sample CT DICOM file
path = examples.get_path("ct")

# Read DICOM file
ds = pydicom.dcmread(path)

# Get the image data
image = ds.pixel_array

# Display the image
plt.imshow(image, cmap="gray")
plt.title("CT DICOM Image")
plt.axis("off")
plt.show()