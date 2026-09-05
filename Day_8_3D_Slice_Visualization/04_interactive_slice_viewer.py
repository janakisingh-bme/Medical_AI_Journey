import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from pathlib import Path


# ==========================================
# 1. PROJECT PATHS
# ==========================================

BASE_DIR = Path(__file__).resolve().parent

input_path = BASE_DIR / "data" / "brain_T1w.nii.gz"


# ==========================================
# 2. LOAD BRAIN MRI
# ==========================================

print("=" * 60)
print("          INTERACTIVE BRAIN MRI VIEWER")
print("=" * 60)

print("\n[1] Loading MRI...")

image = sitk.ReadImage(str(input_path))

print("MRI loaded successfully!")


# ==========================================
# 3. REORIENT IMAGE
# ==========================================

image = sitk.DICOMOrient(
    image,
    "LPS"
)


# ==========================================
# 4. CONVERT TO NUMPY
# ==========================================

volume = sitk.GetArrayFromImage(image)

print("\n[2] IMAGE INFORMATION")

print("Volume shape:", volume.shape)
print("Dimensions:", volume.ndim)


# ==========================================
# 5. GET NUMBER OF SLICES
# ==========================================

num_slices = volume.shape[0]

print("Total slices:", num_slices)


# ==========================================
# 6. START AT MIDDLE SLICE
# ==========================================

initial_slice = num_slices // 2


# ==========================================
# 7. CREATE FIGURE
# ==========================================

fig, ax = plt.subplots(
    figsize=(7, 7)
)

plt.subplots_adjust(
    bottom=0.18
)


# ==========================================
# 8. DISPLAY INITIAL SLICE
# ==========================================

image_display = ax.imshow(
    volume[initial_slice],
    cmap="gray",
    origin="lower"
)

ax.set_title(
    f"Brain MRI - Slice {initial_slice}"
)

ax.axis("off")


# ==========================================
# 9. CREATE SLIDER
# ==========================================

slider_axis = plt.axes(
    [0.20, 0.07, 0.60, 0.03]
)

slice_slider = Slider(
    slider_axis,
    "Slice",
    0,
    num_slices - 1,
    valinit=initial_slice,
    valstep=1
)


# ==========================================
# 10. UPDATE FUNCTION
# ==========================================

def update_slice(value):

    slice_index = int(slice_slider.val)

    image_display.set_data(
        volume[slice_index]
    )

    ax.set_title(
        f"Brain MRI - Slice {slice_index}"
    )

    fig.canvas.draw_idle()


# ==========================================
# 11. CONNECT SLIDER
# ==========================================

slice_slider.on_changed(
    update_slice
)


# ==========================================
# 12. DISPLAY VIEWER
# ==========================================

print("\n[3] Interactive viewer ready!")

print("Move the slider to browse through the MRI slices.")

plt.show()