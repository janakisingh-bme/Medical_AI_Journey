import SimpleITK as sitk
import numpy as np
from pathlib import Path

# Get project directory
BASE_DIR = Path(__file__).resolve().parent

# NIfTI file path
nifti_path = BASE_DIR / "data" / "minimal.nii"

# Read NIfTI
image = sitk.ReadImage(str(nifti_path))

# Convert to NumPy
image_array = sitk.GetArrayFromImage(image)

# Calculate statistics
print("===== NIfTI Volume Statistics =====")

print("Shape:", image_array.shape)
print("Data type:", image_array.dtype)
print("Number of voxels:", image_array.size)

print("\nMinimum:", np.min(image_array))
print("Maximum:", np.max(image_array))
print("Mean:", np.mean(image_array))
print("Median:", np.median(image_array))
print("Standard deviation:", np.std(image_array))