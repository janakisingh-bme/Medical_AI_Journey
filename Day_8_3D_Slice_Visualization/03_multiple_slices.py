import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


# ==========================================
# 1. PROJECT PATHS
# ==========================================

BASE_DIR = Path(__file__).resolve().parent

input_path = BASE_DIR / "data" / "brain_T1w.nii.gz"
output_dir = BASE_DIR / "outputs"

output_dir.mkdir(exist_ok=True)

output_path = output_dir / "multiple_brain_slices.png"


# ==========================================
# 2. LOAD BRAIN MRI
# ==========================================

print("=" * 60)
print("       ORIENTED BRAIN MRI SLICE VIEWER")
print("=" * 60)

print("\n[1] Loading NIfTI image...")

image = sitk.ReadImage(str(input_path))

print("NIfTI loaded successfully!")


# ==========================================
# 3. DISPLAY ORIGINAL ORIENTATION
# ==========================================

print("\n[2] ORIGINAL IMAGE INFORMATION")

print("Size:", image.GetSize())
print("Spacing:", image.GetSpacing())
print("Direction:", image.GetDirection())


# ==========================================
# 4. REORIENT TO STANDARD ORIENTATION
# ==========================================

print("\n[3] REORIENTING IMAGE")

image_oriented = sitk.DICOMOrient(
    image,
    "LPS"
)

print("Image reoriented to LPS orientation.")


# ==========================================
# 5. CONVERT TO NUMPY
# ==========================================

volume = sitk.GetArrayFromImage(
    image_oriented
)

print("\n[4] NUMPY INFORMATION")

print("Shape:", volume.shape)
print("Dimensions:", volume.ndim)
print("Total voxels:", volume.size)


# ==========================================
# 6. NUMBER OF AXIAL SLICES
# ==========================================

num_slices = volume.shape[0]

print("\n[5] SLICE INFORMATION")

print("Total axial slices:", num_slices)


# ==========================================
# 7. SELECT EVENLY SPACED SLICES
# ==========================================

slice_indices = np.linspace(
    0,
    num_slices - 1,
    10,
    dtype=int
)

print("Selected slices:")
print(slice_indices)


# ==========================================
# 8. CREATE FIGURE
# ==========================================

fig, axes = plt.subplots(
    2,
    5,
    figsize=(15, 7)
)


# ==========================================
# 9. DISPLAY AXIAL SLICES
# ==========================================

for ax, index in zip(
    axes.flat,
    slice_indices
):

    ax.imshow(
        volume[index],
        cmap="gray",
        origin="lower"
    )

    ax.set_title(
        f"Axial Slice {index}"
    )

    ax.axis("off")


# ==========================================
# 10. TITLE
# ==========================================

plt.suptitle(
    "T1-Weighted Brain MRI - Axial Slices",
    fontsize=16
)


# ==========================================
# 11. LAYOUT
# ==========================================

plt.tight_layout(
    rect=[0, 0, 1, 0.95]
)


# ==========================================
# 12. SAVE
# ==========================================

plt.savefig(
    output_path,
    dpi=300,
    bbox_inches="tight"
)

print("\n[6] OUTPUT SAVED")

print("File:", output_path)


# ==========================================
# 13. DISPLAY
# ==========================================

plt.show()


# ==========================================
# FINAL SUMMARY
# ==========================================

print("\n" + "=" * 60)
print("             VISUALIZATION COMPLETE")
print("=" * 60)

print("\nOrientation: LPS")
print("Slices displayed:", len(slice_indices))
print("Output:", output_path)

print("\n" + "=" * 60)