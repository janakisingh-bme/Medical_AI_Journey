import SimpleITK as sitk
import matplotlib.pyplot as plt
from pathlib import Path

# Get project directory
BASE_DIR = Path(__file__).resolve().parent

# NIfTI file path
nifti_path = BASE_DIR / "data" / "minimal.nii"

# Read NIfTI image
image = sitk.ReadImage(str(nifti_path))

# Convert to NumPy array
image_array = sitk.GetArrayFromImage(image)

print("Volume shape:", image_array.shape)

# Number of slices
num_slices = image_array.shape[0]

# Create figure
fig, axes = plt.subplots(2, 5, figsize=(12, 5))

# Display all slices
for i, ax in enumerate(axes.flat):

    ax.imshow(image_array[i], cmap="gray")
    ax.set_title(f"Slice {i}")
    ax.axis("off")

plt.suptitle("NIfTI Volume Slices")
plt.tight_layout()
plt.show()