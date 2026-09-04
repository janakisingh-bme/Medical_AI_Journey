import SimpleITK as sitk
from pathlib import Path

# Get project directory
BASE_DIR = Path(__file__).resolve().parent

# NIfTI file path
nifti_path = BASE_DIR / "data" / "minimal.nii"

# Read NIfTI image
image = sitk.ReadImage(str(nifti_path))

print("========== NIfTI METADATA ==========")

print("Image Size      :", image.GetSize())
print("Image Dimension :", image.GetDimension())
print("Image Spacing   :", image.GetSpacing())
print("Image Origin    :", image.GetOrigin())
print("Image Direction :", image.GetDirection())
print("Pixel Type      :", image.GetPixelIDTypeAsString())