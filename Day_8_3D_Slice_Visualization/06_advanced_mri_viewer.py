import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from pathlib import Path


# ============================================================
# 1. PROJECT PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

input_path = BASE_DIR / "data" / "brain_T1w.nii.gz"
output_dir = BASE_DIR / "outputs"

output_dir.mkdir(exist_ok=True)


# ============================================================
# 2. LOAD MRI
# ============================================================

print("=" * 70)
print("              ADVANCED 3D BRAIN MRI VIEWER")
print("=" * 70)

print("\n[1] Loading MRI...")

image = sitk.ReadImage(str(input_path))

# Standardize orientation
image = sitk.DICOMOrient(image, "LPS")

# Convert to NumPy
volume = sitk.GetArrayFromImage(image)

print("MRI loaded successfully!")


# ============================================================
# 3. VOLUME INFORMATION
# ============================================================

z_size, y_size, x_size = volume.shape

print("\n[2] VOLUME INFORMATION")

print("Shape:", volume.shape)
print("Z:", z_size)
print("Y:", y_size)
print("X:", x_size)

print("Spacing:", image.GetSpacing())


# ============================================================
# 4. INITIAL VOXEL
# ============================================================

z_index = z_size // 2
y_index = y_size // 2
x_index = x_size // 2


# ============================================================
# 5. CREATE FIGURE
# ============================================================

fig, axes = plt.subplots(
    1,
    3,
    figsize=(15, 6)
)

plt.subplots_adjust(
    bottom=0.28,
    top=0.88,
    wspace=0.15
)


# ============================================================
# 6. DISPLAY INITIAL IMAGES
# ============================================================

axial_display = axes[0].imshow(
    volume[z_index, :, :],
    cmap="gray",
    origin="lower"
)

coronal_display = axes[1].imshow(
    volume[:, y_index, :],
    cmap="gray",
    origin="lower"
)

sagittal_display = axes[2].imshow(
    volume[:, :, x_index],
    cmap="gray",
    origin="lower"
)


# ============================================================
# 7. TITLES
# ============================================================

axes[0].set_title(
    f"Axial\nZ = {z_index}"
)

axes[1].set_title(
    f"Coronal\nY = {y_index}"
)

axes[2].set_title(
    f"Sagittal\nX = {x_index}"
)


for ax in axes:
    ax.axis("off")


# ============================================================
# 8. CROSSHAIRS
# ============================================================

axial_vertical = axes[0].axvline(
    x_index,
    linewidth=1
)

axial_horizontal = axes[0].axhline(
    y_index,
    linewidth=1
)


coronal_vertical = axes[1].axvline(
    x_index,
    linewidth=1
)

coronal_horizontal = axes[1].axhline(
    z_index,
    linewidth=1
)


sagittal_vertical = axes[2].axvline(
    y_index,
    linewidth=1
)

sagittal_horizontal = axes[2].axhline(
    z_index,
    linewidth=1
)


# ============================================================
# 9. INFORMATION TEXT
# ============================================================

info_text = fig.text(
    0.5,
    0.93,
    "",
    ha="center",
    fontsize=11
)


# ============================================================
# 10. SLIDER — Z
# ============================================================

z_axis = plt.axes(
    [0.20, 0.18, 0.60, 0.03]
)

z_slider = Slider(
    z_axis,
    "Z",
    0,
    z_size - 1,
    valinit=z_index,
    valstep=1
)


# ============================================================
# 11. SLIDER — Y
# ============================================================

y_axis = plt.axes(
    [0.20, 0.12, 0.60, 0.03]
)

y_slider = Slider(
    y_axis,
    "Y",
    0,
    y_size - 1,
    valinit=y_index,
    valstep=1
)


# ============================================================
# 12. SLIDER — X
# ============================================================

x_axis = plt.axes(
    [0.20, 0.06, 0.60, 0.03]
)

x_slider = Slider(
    x_axis,
    "X",
    0,
    x_size - 1,
    valinit=x_index,
    valstep=1
)


# ============================================================
# 13. UPDATE VIEW
# ============================================================

def update_view():

    global z_index
    global y_index
    global x_index

    z_index = int(z_slider.val)
    y_index = int(y_slider.val)
    x_index = int(x_slider.val)

    # ----------------------------------------
    # Update images
    # ----------------------------------------

    axial_display.set_data(
        volume[z_index, :, :]
    )

    coronal_display.set_data(
        volume[:, y_index, :]
    )

    sagittal_display.set_data(
        volume[:, :, x_index]
    )

    # ----------------------------------------
    # Update crosshairs
    # ----------------------------------------

    axial_vertical.set_xdata(
        [x_index, x_index]
    )

    axial_horizontal.set_ydata(
        [y_index, y_index]
    )

    coronal_vertical.set_xdata(
        [x_index, x_index]
    )

    coronal_horizontal.set_ydata(
        [z_index, z_index]
    )

    sagittal_vertical.set_xdata(
        [y_index, y_index]
    )

    sagittal_horizontal.set_ydata(
        [z_index, z_index]
    )

    # ----------------------------------------
    # Update titles
    # ----------------------------------------

    axes[0].set_title(
        f"Axial\nZ = {z_index}"
    )

    axes[1].set_title(
        f"Coronal\nY = {y_index}"
    )

    axes[2].set_title(
        f"Sagittal\nX = {x_index}"
    )

    # ----------------------------------------
    # Get voxel intensity
    # ----------------------------------------

    voxel_value = volume[
        z_index,
        y_index,
        x_index
    ]

    # ----------------------------------------
    # Update information
    # ----------------------------------------

    info_text.set_text(
        f"Voxel → X: {x_index}   "
        f"Y: {y_index}   "
        f"Z: {z_index}   |   "
        f"Intensity: {voxel_value:.2f}"
    )

    fig.canvas.draw_idle()


# ============================================================
# 14. CONNECT SLIDERS
# ============================================================

z_slider.on_changed(
    lambda value: update_view()
)

y_slider.on_changed(
    lambda value: update_view()
)

x_slider.on_changed(
    lambda value: update_view()
)


# ============================================================
# 15. MOUSE CLICK FUNCTION
# ============================================================

def on_click(event):

    global x_index
    global y_index
    global z_index

    if event.inaxes not in axes:
        return

    if event.xdata is None or event.ydata is None:
        return

    # ----------------------------------------
    # Click in AXIAL
    # ----------------------------------------

    if event.inaxes == axes[0]:

        x_index = int(round(event.xdata))
        y_index = int(round(event.ydata))

        x_index = np.clip(
            x_index,
            0,
            x_size - 1
        )

        y_index = np.clip(
            y_index,
            0,
            y_size - 1
        )

        x_slider.set_val(x_index)
        y_slider.set_val(y_index)

    # ----------------------------------------
    # Click in CORONAL
    # ----------------------------------------

    elif event.inaxes == axes[1]:

        x_index = int(round(event.xdata))
        z_index = int(round(event.ydata))

        x_index = np.clip(
            x_index,
            0,
            x_size - 1
        )

        z_index = np.clip(
            z_index,
            0,
            z_size - 1
        )

        x_slider.set_val(x_index)
        z_slider.set_val(z_index)

    # ----------------------------------------
    # Click in SAGITTAL
    # ----------------------------------------

    elif event.inaxes == axes[2]:

        y_index = int(round(event.xdata))
        z_index = int(round(event.ydata))

        y_index = np.clip(
            y_index,
            0,
            y_size - 1
        )

        z_index = np.clip(
            z_index,
            0,
            z_size - 1
        )

        y_slider.set_val(y_index)
        z_slider.set_val(z_index)


# ============================================================
# 16. CONNECT MOUSE
# ============================================================

fig.canvas.mpl_connect(
    "button_press_event",
    on_click
)


# ============================================================
# 17. SAVE BUTTON
# ============================================================

button_axis = plt.axes(
    [0.82, 0.01, 0.12, 0.035]
)

save_button = Button(
    button_axis,
    "Save View"
)


# ============================================================
# 18. SAVE CURRENT VIEW
# ============================================================

def save_view(event):

    save_path = (
        output_dir /
        f"crosshair_X{x_index}_Y{y_index}_Z{z_index}.png"
    )

    fig.savefig(
        save_path,
        dpi=300,
        bbox_inches="tight"
    )

    print("\nView saved!")
    print("Output:", save_path)


save_button.on_clicked(
    save_view
)


# ============================================================
# 19. INITIAL UPDATE
# ============================================================

update_view()


# ============================================================
# 20. DISPLAY
# ============================================================

print("\n[3] ADVANCED VIEWER READY")

print("\nControls:")
print("  • Move X/Y/Z sliders")
print("  • Click any MRI plane")
print("  • Crosshair updates automatically")
print("  • Voxel intensity is displayed")
print("  • Click 'Save View' to save the current view")

print("\nClose the window when finished.")


plt.suptitle(
    "Advanced 3D Brain MRI Crosshair Viewer",
    fontsize=16
)

plt.show()


# ============================================================
# 21. FINAL
# ============================================================

print("\n" + "=" * 70)
print("                  VIEWER CLOSED")
print("=" * 70)