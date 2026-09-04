import SimpleITK as sitk
import numpy as np
from pathlib import Path

# Get project directory
BASE_DIR = Path(__file__).resolve().parent

# Input NIfTI path
input_path = BASE_DIR / "data" / "minimal.nii"

# Output NIfTI path
output_path = BASE_DIR / "data" / "processed.nii"

# Read NIfTI image
image = sitk.ReadImage(str(input_path))

# Convert to NumPy
image_array = sitk.GetArrayFromImage(image)

print("Original shape:", image_array.shape)
print("Original min:", np.min(image_array))
print("Original max:", np.max(image_array))

# -------------------------------
# Normalize voxel values
# -------------------------------

image_min = np.min(image_array)
image_max = np.max(image_array)

normalized_array = (
    (image_array - image_min)
    / (image_max - image_min)
)

# Convert from 0–1 to 0–255
normalized_array = (normalized_array * 255).astype(np.uint8)

print("\nAfter normalization:")
print("Minimum:", np.min(normalized_array))
print("Maximum:", np.max(normalized_array))

# -------------------------------
# Convert NumPy back to SimpleITK
# -------------------------------

processed_image = sitk.GetImageFromArray(normalized_array)

# Preserve spatial information
processed_image.CopyInformation(image)

# Save processed NIfTI
sitk.WriteImage(processed_image, str(output_path))

print("\nProcessed NIfTI saved successfully!")
print("Saved to:", output_path)