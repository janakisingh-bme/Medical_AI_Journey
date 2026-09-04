import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# ==========================================
# 1. Project paths
# ==========================================

BASE_DIR = Path(__file__).resolve().parent
input_path = BASE_DIR / "data" / "minimal.nii"
output_path = BASE_DIR / "data" / "normalized.nii"

# ==========================================
# 2. Read NIfTI
# ==========================================

image = sitk.ReadImage(str(input_path))

print("===== NIfTI MINI PROJECT =====")

print("\nImage information:")
print("Size:", image.GetSize())
print("Spacing:", image.GetSpacing())
print("Origin:", image.GetOrigin())
print("Direction:", image.GetDirection())

# ==========================================
# 3. Convert to NumPy
# ==========================================

volume = sitk.GetArrayFromImage(image)

print("\nNumPy information:")
print("Shape:", volume.shape)
print("Data type:", volume.dtype)
print("Number of dimensions:", volume.ndim)
print("Total voxels:", volume.size)

# ==========================================
# 4. Calculate statistics
# ==========================================

print("\n===== VOXEL STATISTICS =====")

print("Minimum:", np.min(volume))
print("Maximum:", np.max(volume))
print("Mean:", np.mean(volume))
print("Median:", np.median(volume))
print("Standard deviation:", np.std(volume))

# ==========================================
# 5. Normalize volume
# ==========================================

minimum = np.min(volume)
maximum = np.max(volume)

normalized = (volume - minimum) / (maximum - minimum)

print("\n===== NORMALIZATION =====")
print("Normalized minimum:", np.min(normalized))
print("Normalized maximum:", np.max(normalized))

# ==========================================
# 6. Save normalized NIfTI
# ==========================================

normalized_image = sitk.GetImageFromArray(normalized.astype(np.float32))

# Preserve spatial information
normalized_image.CopyInformation(image)

sitk.WriteImage(normalized_image, str(output_path))

print("\nNormalized NIfTI saved:")
print(output_path)

# ==========================================
# 7. Display middle slice
# ==========================================

middle_slice = volume.shape[0] // 2

plt.figure(figsize=(6, 6))

plt.imshow(volume[middle_slice], cmap="gray")

plt.title(f"Middle Slice: {middle_slice}")
plt.axis("off")

plt.show()

print("\n===== PROJECT COMPLETE =====")