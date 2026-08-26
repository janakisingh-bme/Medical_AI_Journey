import pydicom
from pydicom import examples

# Get the path of the sample CT DICOM file
path = examples.get_path("ct")

# Read the DICOM file
ds = pydicom.dcmread(path)

# Display the DICOM information
print(ds)