import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


# ==========================================
# PROJECT PATHS
# ==========================================

BASE_DIR = Path(__file__).resolve().parent

input_path = BASE_DIR / "data" / "minimal.nii"
output_dir = BASE_DIR / "outputs"

output_dir.mkdir(exist_ok=True)

output_path = output_dir / "normalized.nii"


# ==========================================
# 1. READ NIFTI
# ==========================================

print("=" * 55)
print("       NIFTI MEDICAL IMAGE ANALYSIS TOOLKIT")
print("=" * 55)

print("\n[1] Reading NIfTI image...")

image = sitk.ReadImage(str(input_path))

print("NIfTI loaded successfully!")


# ==========================================
# 2. IMAGE INFORMATION
# ==========================================

print("\n[2] IMAGE INFORMATION")

print("Size:", image.GetSize())
print("Dimension:", image.GetDimension())
print("Spacing:", image.GetSpacing())
print("Origin:", image.GetOrigin())


# ==========================================
# 3. CONVERT NIFTI TO NUMPY
# ==========================================

volume = sitk.GetArrayFromImage(image)

print("\n[3] NUMPY INFORMATION")

print("Shape:", volume.shape)
print("Dimensions:", volume.ndim)
print("Data type:", volume.dtype)
print("Total voxels:", volume.size)


# ==========================================
# 4. VOXEL STATISTICS
# ==========================================

print("\n[4] VOXEL STATISTICS")

minimum = np.min(volume)
maximum = np.max(volume)
mean = np.mean(volume)
median = np.median(volume)
std = np.std(volume)

print("Minimum:", minimum)
print("Maximum:", maximum)
print("Mean:", mean)
print("Median:", median)
print("Standard deviation:", std)


# ==========================================
# 5. DISPLAY MIDDLE SLICE
# ==========================================

middle_slice = volume.shape[0] // 2

print("\n[5] MIDDLE SLICE")
print("Total slices:", volume.shape[0])
print("Displaying slice:", middle_slice)

plt.figure(figsize=(6, 6))

plt.imshow(
    volume[middle_slice],
    cmap="gray"
)

plt.title(f"Middle Slice - {middle_slice}")
plt.axis("off")

plt.show()


# ==========================================
# 6. DISPLAY ALL SLICES
# ==========================================

print("\n[6] DISPLAYING ALL SLICES")

num_slices = volume.shape[0]

fig, axes = plt.subplots(
    2,
    5,
    figsize=(12, 5)
)

for i, ax in enumerate(axes.flat):

    if i < num_slices:
        ax.imshow(
            volume[i],
            cmap="gray"
        )

        ax.set_title(f"Slice {i}")
        ax.axis("off")

    else:
        ax.axis("off")


plt.suptitle("NIfTI Volume - All Slices")
plt.tight_layout()
plt.show()


# ==========================================
# 7. NORMALIZATION
# ==========================================

print("\n[7] NORMALIZATION")

normalized = (
    (volume - minimum)
    / (maximum - minimum)
)

print("Normalized minimum:", np.min(normalized))
print("Normalized maximum:", np.max(normalized))


# ==========================================
# 8. SAVE NORMALIZED NIFTI
# ==========================================

print("\n[8] SAVING NORMALIZED NIFTI")

normalized_image = sitk.GetImageFromArray(
    normalized.astype(np.float32)
)

# Preserve original spatial information
normalized_image.CopyInformation(image)

sitk.WriteImage(
    normalized_image,
    str(output_path)
)

print("Normalized NIfTI saved successfully!")
print("Output:", output_path)


# ==========================================
# FINAL SUMMARY
# ==========================================

print("\n" + "=" * 55)
print("                  PROJECT COMPLETE")
print("=" * 55)

print("\nVolume shape:", volume.shape)
print("Total voxels:", volume.size)
print("Voxel range:", minimum, "to", maximum)
print("Mean intensity:", mean)

print("\nGenerated file:")
print("outputs/normalized.nii")