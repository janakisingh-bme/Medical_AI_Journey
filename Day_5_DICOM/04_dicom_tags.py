import pydicom
from pydicom import examples

# Get sample CT DICOM file
path = examples.get_path("ct")

# Read DICOM file
ds = pydicom.dcmread(path)

# Display selected DICOM tags
print("DICOM TAG INFORMATION")
print("---------------------")

print("Patient Name:", ds.get("PatientName", "Not available"))
print("Patient ID:", ds.get("PatientID", "Not available"))
print("Modality:", ds.get("Modality", "Not available"))
print("Study Date:", ds.get("StudyDate", "Not available"))
print("Rows:", ds.get("Rows", "Not available"))
print("Columns:", ds.get("Columns", "Not available"))