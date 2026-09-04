import SimpleITK as sitk
import numpy as np
from pathlib import Path

# Get project directory
BASE_DIR = Path(__file__).resolve().parent

# NIfTI file path
nifti_path = BASE_DIR / "data" / "minimal.nii"

# Read NIfTI image
image = sitk.ReadImage(str(nifti_path))

# Convert NIfTI → NumPy
image_array = sitk.GetArrayFromImage(image)

print("Successfully converted NIfTI to NumPy!")

print("Array shape:", image_array.shape)
print("Data type:", image_array.dtype)
print("Number of dimensions:", image_array.ndim)
print("Total number of voxels:", image_array.size)

print("\nFirst slice shape:", image_array[0].shape)

print("\nFirst voxel value:", image_array[0, 0, 0])

print("\nMinimum voxel value:", np.min(image_array))
print("Maximum voxel value:", np.max(image_array))