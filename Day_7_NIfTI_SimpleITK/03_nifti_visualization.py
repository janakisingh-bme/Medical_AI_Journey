import SimpleITK as sitk
import matplotlib.pyplot as plt
from pathlib import Path

# Get project directory
BASE_DIR = Path(__file__).resolve().parent

# NIfTI file path
nifti_path = BASE_DIR / "data" / "minimal.nii"

# Read NIfTI image
image = sitk.ReadImage(str(nifti_path))

# Convert SimpleITK image to NumPy array
image_array = sitk.GetArrayFromImage(image)

print("Image shape:", image_array.shape)

# Select middle slice
middle_slice = image_array.shape[0] // 2

# Display middle slice
plt.imshow(image_array[middle_slice], cmap="gray")
plt.title(f"Middle Slice - {middle_slice}")
plt.axis("off")
plt.show()