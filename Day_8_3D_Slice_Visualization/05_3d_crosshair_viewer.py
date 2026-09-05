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
# 2. LOAD MRI
# ==========================================

print("=" * 60)
print("          3D BRAIN MRI CROSSHAIR VIEWER")
print("=" * 60)

print("\n[1] Loading MRI...")

image = sitk.ReadImage(str(input_path))

# Standardize orientation
image = sitk.DICOMOrient(image, "LPS")

volume = sitk.GetArrayFromImage(image)

print("MRI loaded successfully!")
print("Volume shape:", volume.shape)
print("Dimensions:", volume.ndim)


# ==========================================
# 3. GET DIMENSIONS
# ==========================================

z, y, x = volume.shape

print("\nVolume dimensions:")
print("Z:", z)
print("Y:", y)
print("X:", x)


# ==========================================
# 4. INITIAL CENTER POINT
# ==========================================

current_z = z // 2
current_y = y // 2
current_x = x // 2


# ==========================================
# 5. CREATE FIGURE
# ==========================================

fig, axes = plt.subplots(
    1,
    3,
    figsize=(15, 5)
)

plt.subplots_adjust(
    bottom=0.22,
    wspace=0.15
)


# ==========================================
# 6. EXTRACT INITIAL VIEWS
# ==========================================

axial = volume[current_z, :, :]
coronal = volume[:, current_y, :]
sagittal = volume[:, :, current_x]


# ==========================================
# 7. DISPLAY AXIAL
# ==========================================

axial_display = axes[0].imshow(
    axial,
    cmap="gray",
    origin="lower"
)

axes[0].set_title(
    f"Axial | Z = {current_z}"
)

axes[0].axis("off")


# ==========================================
# 8. DISPLAY CORONAL
# ==========================================

coronal_display = axes[1].imshow(
    coronal,
    cmap="gray",
    origin="lower"
)

axes[1].set_title(
    f"Coronal | Y = {current_y}"
)

axes[1].axis("off")


# ==========================================
# 9. DISPLAY SAGITTAL
# ==========================================

sagittal_display = axes[2].imshow(
    sagittal,
    cmap="gray",
    origin="lower"
)

axes[2].set_title(
    f"Sagittal | X = {current_x}"
)

axes[2].axis("off")


# ==========================================
# 10. ADD CROSSHAIRS
# ==========================================

axial_vertical = axes[0].axvline(
    current_x,
    linewidth=1
)

axial_horizontal = axes[0].axhline(
    current_y,
    linewidth=1
)


coronal_vertical = axes[1].axvline(
    current_x,
    linewidth=1
)

coronal_horizontal = axes[1].axhline(
    current_z,
    linewidth=1
)


sagittal_vertical = axes[2].axvline(
    current_y,
    linewidth=1
)

sagittal_horizontal = axes[2].axhline(
    current_z,
    linewidth=1
)


# ==========================================
# 11. CREATE Z SLIDER
# ==========================================

z_axis = plt.axes(
    [0.20, 0.13, 0.60, 0.03]
)

z_slider = Slider(
    z_axis,
    "Axial Z",
    0,
    z - 1,
    valinit=current_z,
    valstep=1
)


# ==========================================
# 12. CREATE Y SLIDER
# ==========================================

y_axis = plt.axes(
    [0.20, 0.08, 0.60, 0.03]
)

y_slider = Slider(
    y_axis,
    "Coronal Y",
    0,
    y - 1,
    valinit=current_y,
    valstep=1
)


# ==========================================
# 13. CREATE X SLIDER
# ==========================================

x_axis = plt.axes(
    [0.20, 0.03, 0.60, 0.03]
)

x_slider = Slider(
    x_axis,
    "Sagittal X",
    0,
    x - 1,
    valinit=current_x,
    valstep=1
)


# ==========================================
# 14. UPDATE FUNCTION
# ==========================================

def update(val):

    z_index = int(z_slider.val)
    y_index = int(y_slider.val)
    x_index = int(x_slider.val)

    # Update images
    axial_display.set_data(
        volume[z_index, :, :]
    )

    coronal_display.set_data(
        volume[:, y_index, :]
    )

    sagittal_display.set_data(
        volume[:, :, x_index]
    )

    # Update crosshair positions

    axial_vertical.set_xdata([x_index, x_index])
    axial_horizontal.set_ydata([y_index, y_index])

    coronal_vertical.set_xdata([x_index, x_index])
    coronal_horizontal.set_ydata([z_index, z_index])

    sagittal_vertical.set_xdata([y_index, y_index])
    sagittal_horizontal.set_ydata([z_index, z_index])

    # Update titles

    axes[0].set_title(
        f"Axial | Z = {z_index}"
    )

    axes[1].set_title(
        f"Coronal | Y = {y_index}"
    )

    axes[2].set_title(
        f"Sagittal | X = {x_index}"
    )

    fig.canvas.draw_idle()


# ==========================================
# 15. CONNECT SLIDERS
# ==========================================

z_slider.on_changed(update)
y_slider.on_changed(update)
x_slider.on_changed(update)


# ==========================================
# 16. FINAL TITLE
# ==========================================

fig.suptitle(
    "Interactive 3D Brain MRI Crosshair Viewer",
    fontsize=16
)


# ==========================================
# 17. START VIEWER
# ==========================================

print("\n[2] Interactive viewer ready!")

print("\nUse the sliders to navigate:")
print("  Axial slider    → Z axis")
print("  Coronal slider  → Y axis")
print("  Sagittal slider → X axis")

print("\nClose the viewer when finished.")

plt.show()


# ==========================================
# FINAL
# ==========================================

print("\n" + "=" * 60)
print("             VIEWER CLOSED")
print("=" * 60)