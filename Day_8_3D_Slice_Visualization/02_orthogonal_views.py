import SimpleITK as sitk
import matplotlib.pyplot as plt
from pathlib import Path


# ==========================================
# 1. PROJECT PATHS
# ==========================================

BASE_DIR = Path(__file__).resolve().parent

input_path = BASE_DIR / "data" / "brain_T1w.nii.gz"
output_dir = BASE_DIR / "outputs"

output_dir.mkdir(exist_ok=True)

output_path = output_dir / "orthogonal_views.png"


# ==========================================
# 2. LOAD REAL BRAIN MRI
# ==========================================

print("=" * 55)
print("          3D BRAIN MRI VISUALIZATION")
print("=" * 55)

print("\n[1] Loading NIfTI image...")

image = sitk.ReadImage(str(input_path))

print("NIfTI loaded successfully!")


# ==========================================
# 3. CONVERT TO NUMPY
# ==========================================

volume = sitk.GetArrayFromImage(image)

print("\n[2] IMAGE INFORMATION")

print("Volume shape:", volume.shape)
print("Dimensions:", volume.ndim)
print("Image size:", image.GetSize())
print("Voxel spacing:", image.GetSpacing())


# ==========================================
# 4. GET VOLUME DIMENSIONS
# ==========================================

z, y, x = volume.shape

print("\n[3] VOLUME DIMENSIONS")

print("Z:", z)
print("Y:", y)
print("X:", x)


# ==========================================
# 5. FIND MIDDLE SLICES
# ==========================================

middle_z = z // 2
middle_y = y // 2
middle_x = x // 2

print("\n[4] SELECTED MIDDLE SLICES")

print("Axial:", middle_z)
print("Coronal:", middle_y)
print("Sagittal:", middle_x)


# ==========================================
# 6. EXTRACT THREE VIEWS
# ==========================================

axial = volume[middle_z, :, :]

coronal = volume[:, middle_y, :]

sagittal = volume[:, :, middle_x]


# ==========================================
# 7. CREATE FIGURE
# ==========================================

fig, axes = plt.subplots(
    1,
    3,
    figsize=(15, 5)
)


# ==========================================
# 8. AXIAL VIEW
# ==========================================

axes[0].imshow(
    axial,
    cmap="gray",
    origin="lower"
)

axes[0].set_title(
    f"Axial View\nSlice {middle_z}"
)

axes[0].axis("off")


# ==========================================
# 9. CORONAL VIEW
# ==========================================

axes[1].imshow(
    coronal,
    cmap="gray",
    origin="lower"
)

axes[1].set_title(
    f"Coronal View\nSlice {middle_y}"
)

axes[1].axis("off")


# ==========================================
# 10. SAGITTAL VIEW
# ==========================================

axes[2].imshow(
    sagittal,
    cmap="gray",
    origin="lower"
)

axes[2].set_title(
    f"Sagittal View\nSlice {middle_x}"
)

axes[2].axis("off")


# ==========================================
# 11. FINAL TITLE
# ==========================================

plt.suptitle(
    "Brain MRI - Orthogonal Views",
    fontsize=16
)

plt.tight_layout()


# ==========================================
# 12. SAVE FIGURE
# ==========================================

plt.savefig(
    output_path,
    dpi=300,
    bbox_inches="tight"
)

print("\n[5] VISUALIZATION SAVED")

print("Output:", output_path)


# ==========================================
# 13. DISPLAY
# ==========================================

plt.show()


# ==========================================
# FINAL SUMMARY
# ==========================================

print("\n" + "=" * 55)
print("              VISUALIZATION COMPLETE")
print("=" * 55)

print("\nGenerated file:")
print("outputs/orthogonal_views.png")