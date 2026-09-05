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
# PROJECT HEADER
# ==========================================

print("=" * 55)
print("       NIFTI MEDICAL IMAGE ANALYSIS TOOLKIT")
print("=" * 55)


# ==========================================
# 1. CHECK INPUT FILE
# ==========================================

print("\n[1] CHECKING NIfTI FILE...")

print("Expected file:")
print(input_path)

print("\nFile exists:", input_path.exists())

if not input_path.exists():

    print("\nERROR: NIfTI file was not found!")

    print("\nFiles currently inside data folder:")

    data_folder = BASE_DIR / "data"

    if data_folder.exists():

        files = list(data_folder.iterdir())

        if files:
            for file in files:
                print(" -", file.name)
        else:
            print(" - Data folder is empty")

    else:
        print(" - Data folder does not exist")

    print("\nPlease place 'minimal.nii' inside:")
    print(data_folder)

    raise FileNotFoundError(
        f"NIfTI file not found: {input_path}"
    )


# ==========================================
# 2. READ NIFTI
# ==========================================

print("\n[2] READING NIfTI IMAGE...")

try:

    image = sitk.ReadImage(str(input_path))

except Exception as e:

    print("\nERROR: SimpleITK could not read the NIfTI file.")
    print("\nFile:", input_path)
    print("\nOriginal error:")
    print(e)

    raise


print("NIfTI loaded successfully!")


# ==========================================
# 3. IMAGE INFORMATION
# ==========================================

print("\n[3] IMAGE INFORMATION")

print("Size:", image.GetSize())
print("Dimension:", image.GetDimension())
print("Spacing:", image.GetSpacing())
print("Origin:", image.GetOrigin())


# ==========================================
# 4. CONVERT NIFTI TO NUMPY
# ==========================================

print("\n[4] CONVERTING NIFTI TO NUMPY")

volume = sitk.GetArrayFromImage(image)

print("Conversion successful!")

print("\nNumPy Information:")
print("Shape:", volume.shape)
print("Dimensions:", volume.ndim)
print("Data type:", volume.dtype)
print("Total voxels:", volume.size)


# ==========================================
# 5. VOXEL STATISTICS
# ==========================================

print("\n[5] VOXEL STATISTICS")

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
# 6. DISPLAY MIDDLE SLICE
# ==========================================

print("\n[6] MIDDLE SLICE")

num_slices = volume.shape[0]

middle_slice = num_slices // 2

print("Total slices:", num_slices)
print("Displaying slice:", middle_slice)

plt.figure(figsize=(6, 6))

plt.imshow(
    volume[middle_slice],
    cmap="gray"
)

plt.title(f"Middle Slice - {middle_slice}")
plt.axis("off")

plt.tight_layout()
plt.show()


# ==========================================
# 7. DISPLAY ALL SLICES
# ==========================================

print("\n[7] DISPLAYING ALL SLICES")

# Number of slices to display
display_slices = min(num_slices, 10)

fig, axes = plt.subplots(
    2,
    5,
    figsize=(12, 5)
)

for i, ax in enumerate(axes.flat):

    if i < display_slices:

        ax.imshow(
            volume[i],
            cmap="gray"
        )

        ax.set_title(f"Slice {i}")
        ax.axis("off")

    else:

        ax.axis("off")


plt.suptitle("NIfTI Volume - Slices")
plt.tight_layout()
plt.show()


# ==========================================
# 8. NORMALIZATION
# ==========================================

print("\n[8] NORMALIZATION")

# Prevent division by zero
if maximum == minimum:

    normalized = np.zeros_like(
        volume,
        dtype=np.float32
    )

else:

    normalized = (
        (volume - minimum)
        / (maximum - minimum)
    )


print("Normalized minimum:", np.min(normalized))
print("Normalized maximum:", np.max(normalized))


# ==========================================
# 9. SAVE NORMALIZED NIFTI
# ==========================================

print("\n[9] SAVING NORMALIZED NIFTI")

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
# 10. FINAL SUMMARY
# ==========================================

print("\n" + "=" * 55)
print("                  PROJECT COMPLETE")
print("=" * 55)

print("\nVolume shape:", volume.shape)
print("Total voxels:", volume.size)
print("Voxel range:", minimum, "to", maximum)
print("Mean intensity:", mean)
print("Median intensity:", median)
print("Standard deviation:", std)

print("\nGenerated file:")
print(output_path)

print("\n" + "=" * 55)
print("                    DONE")
print("=" * 55)