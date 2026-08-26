import pydicom
from pydicom import examples

# Get sample CT DICOM file
path = examples.get_path("ct")

# Read DICOM file
ds = pydicom.dcmread(path)

# Extract important metadata
print("DICOM file loaded successfully!")
print("Patient Name:", ds.PatientName)
print("Modality:", ds.Modality)
print("Image Rows:", ds.Rows)
print("Image Columns:", ds.Columns)