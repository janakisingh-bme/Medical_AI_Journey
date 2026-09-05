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
print("            MRI ANALYSIS DASHBOARD")
print("=" * 70)

print("\n[1] Loading MRI...")

image = sitk.ReadImage(str(input_path))

# Standard orientation
image = sitk.DICOMOrient(
    image,
    "LPS"
)

volume = sitk.GetArrayFromImage(
    image
).astype(np.float32)

print("MRI loaded successfully!")


# ============================================================
# 3. IMAGE INFORMATION
# ============================================================

z_size, y_size, x_size = volume.shape

spacing_x, spacing_y, spacing_z = image.GetSpacing()

minimum = volume.min()
maximum = volume.max()
mean = volume.mean()
std = volume.std()

print("\n[2] IMAGE INFORMATION")

print("Shape:", volume.shape)
print("Dimensions:", volume.ndim)

print(
    "Spacing:",
    image.GetSpacing()
)

print("Minimum:", minimum)
print("Maximum:", maximum)
print("Mean:", mean)
print("Standard deviation:", std)


# ============================================================
# 4. INITIAL POSITION
# ============================================================

z_index = z_size // 2
y_index = y_size // 2
x_index = x_size // 2


# ============================================================
# 5. CREATE DASHBOARD
# ============================================================

fig = plt.figure(
    figsize=(16, 9)
)

fig.suptitle(
    "3D Brain MRI Analysis Dashboard",
    fontsize=18
)


# ============================================================
# 6. CREATE AXES
# ============================================================

axial_ax = plt.axes(
    [0.04, 0.55, 0.27, 0.32]
)

coronal_ax = plt.axes(
    [0.36, 0.55, 0.27, 0.32]
)

sagittal_ax = plt.axes(
    [0.68, 0.55, 0.27, 0.32]
)

hist_ax = plt.axes(
    [0.08, 0.16, 0.38, 0.25]
)

info_ax = plt.axes(
    [0.55, 0.16, 0.38, 0.25]
)


# ============================================================
# 7. INITIAL MRI VIEWS
# ============================================================

axial_display = axial_ax.imshow(
    volume[z_index, :, :],
    cmap="gray",
    origin="lower"
)

coronal_display = coronal_ax.imshow(
    volume[:, y_index, :],
    cmap="gray",
    origin="lower"
)

sagittal_display = sagittal_ax.imshow(
    volume[:, :, x_index],
    cmap="gray",
    origin="lower"
)


# ============================================================
# 8. TITLES
# ============================================================

axial_ax.set_title(
    f"Axial | Z = {z_index}"
)

coronal_ax.set_title(
    f"Coronal | Y = {y_index}"
)

sagittal_ax.set_title(
    f"Sagittal | X = {x_index}"
)


for ax in [
    axial_ax,
    coronal_ax,
    sagittal_ax
]:
    ax.axis("off")


# ============================================================
# 9. CROSSHAIRS
# ============================================================

axial_v = axial_ax.axvline(
    x_index,
    linewidth=1
)

axial_h = axial_ax.axhline(
    y_index,
    linewidth=1
)


coronal_v = coronal_ax.axvline(
    x_index,
    linewidth=1
)

coronal_h = coronal_ax.axhline(
    z_index,
    linewidth=1
)


sagittal_v = sagittal_ax.axvline(
    y_index,
    linewidth=1
)

sagittal_h = sagittal_ax.axhline(
    z_index,
    linewidth=1
)


# ============================================================
# 10. HISTOGRAM
# ============================================================

hist_ax.hist(
    volume.flatten(),
    bins=100
)

hist_ax.set_title(
    "MRI Intensity Histogram"
)

hist_ax.set_xlabel(
    "Intensity"
)

hist_ax.set_ylabel(
    "Voxel Count"
)


# ============================================================
# 11. INFORMATION PANEL
# ============================================================

info_ax.axis("off")

info_text = info_ax.text(
    0,
    1,
    "",
    va="top",
    fontsize=11,
    family="monospace"
)


# ============================================================
# 12. SLIDERS
# ============================================================

z_slider_axis = plt.axes(
    [0.18, 0.095, 0.60, 0.025]
)

y_slider_axis = plt.axes(
    [0.18, 0.060, 0.60, 0.025]
)

x_slider_axis = plt.axes(
    [0.18, 0.025, 0.60, 0.025]
)


z_slider = Slider(
    z_slider_axis,
    "Z",
    0,
    z_size - 1,
    valinit=z_index,
    valstep=1
)


y_slider = Slider(
    y_slider_axis,
    "Y",
    0,
    y_size - 1,
    valinit=y_index,
    valstep=1
)


x_slider = Slider(
    x_slider_axis,
    "X",
    0,
    x_size - 1,
    valinit=x_index,
    valstep=1
)


# ============================================================
# 13. UPDATE DASHBOARD
# ============================================================

def update_dashboard():

    global x_index
    global y_index
    global z_index

    x_index = int(
        x_slider.val
    )

    y_index = int(
        y_slider.val
    )

    z_index = int(
        z_slider.val
    )


    # --------------------------------------------------------
    # Update MRI views
    # --------------------------------------------------------

    axial_display.set_data(
        volume[z_index, :, :]
    )

    coronal_display.set_data(
        volume[:, y_index, :]
    )

    sagittal_display.set_data(
        volume[:, :, x_index]
    )


    # --------------------------------------------------------
    # Update crosshairs
    # --------------------------------------------------------

    axial_v.set_xdata(
        [x_index, x_index]
    )

    axial_h.set_ydata(
        [y_index, y_index]
    )


    coronal_v.set_xdata(
        [x_index, x_index]
    )

    coronal_h.set_ydata(
        [z_index, z_index]
    )


    sagittal_v.set_xdata(
        [y_index, y_index]
    )

    sagittal_h.set_ydata(
        [z_index, z_index]
    )


    # --------------------------------------------------------
    # Update titles
    # --------------------------------------------------------

    axial_ax.set_title(
        f"Axial | Z = {z_index}"
    )

    coronal_ax.set_title(
        f"Coronal | Y = {y_index}"
    )

    sagittal_ax.set_title(
        f"Sagittal | X = {x_index}"
    )


    # --------------------------------------------------------
    # Voxel intensity
    # --------------------------------------------------------

    voxel_value = volume[
        z_index,
        y_index,
        x_index
    ]


    # --------------------------------------------------------
    # Physical coordinates
    # --------------------------------------------------------

    physical_point = image.TransformIndexToPhysicalPoint(
        (
            x_index,
            y_index,
            z_index
        )
    )


    physical_x = physical_point[0]
    physical_y = physical_point[1]
    physical_z = physical_point[2]


    # --------------------------------------------------------
    # Update information panel
    # --------------------------------------------------------

    info = f"""
MRI INFORMATION
----------------------------

Volume Shape
{volume.shape}

Voxel Spacing
X: {spacing_x:.2f} mm
Y: {spacing_y:.2f} mm
Z: {spacing_z:.2f} mm


CURRENT VOXEL
----------------------------

X: {x_index}
Y: {y_index}
Z: {z_index}

Intensity:
{voxel_value:.2f}


PHYSICAL POSITION
----------------------------

X: {physical_x:.2f} mm
Y: {physical_y:.2f} mm
Z: {physical_z:.2f} mm


GLOBAL STATISTICS
----------------------------

Min: {minimum:.2f}
Max: {maximum:.2f}
Mean: {mean:.2f}
Std: {std:.2f}
"""

    info_text.set_text(
        info
    )

    fig.canvas.draw_idle()


# ============================================================
# 14. CONNECT SLIDERS
# ============================================================

z_slider.on_changed(
    lambda value:
    update_dashboard()
)

y_slider.on_changed(
    lambda value:
    update_dashboard()
)

x_slider.on_changed(
    lambda value:
    update_dashboard()
)


# ============================================================
# 15. CLICK NAVIGATION
# ============================================================

def on_click(event):

    if event.xdata is None:
        return

    if event.ydata is None:
        return


    # --------------------------------------------------------
    # AXIAL
    # --------------------------------------------------------

    if event.inaxes == axial_ax:

        x = int(
            round(event.xdata)
        )

        y = int(
            round(event.ydata)
        )

        x = np.clip(
            x,
            0,
            x_size - 1
        )

        y = np.clip(
            y,
            0,
            y_size - 1
        )

        x_slider.set_val(x)
        y_slider.set_val(y)


    # --------------------------------------------------------
    # CORONAL
    # --------------------------------------------------------

    elif event.inaxes == coronal_ax:

        x = int(
            round(event.xdata)
        )

        z = int(
            round(event.ydata)
        )

        x = np.clip(
            x,
            0,
            x_size - 1
        )

        z = np.clip(
            z,
            0,
            z_size - 1
        )

        x_slider.set_val(x)
        z_slider.set_val(z)


    # --------------------------------------------------------
    # SAGITTAL
    # --------------------------------------------------------

    elif event.inaxes == sagittal_ax:

        y = int(
            round(event.xdata)
        )

        z = int(
            round(event.ydata)
        )

        y = np.clip(
            y,
            0,
            y_size - 1
        )

        z = np.clip(
            z,
            0,
            z_size - 1
        )

        y_slider.set_val(y)
        z_slider.set_val(z)


fig.canvas.mpl_connect(
    "button_press_event",
    on_click
)


# ============================================================
# 16. SAVE BUTTON
# ============================================================

save_axis = plt.axes(
    [0.82, 0.02, 0.12, 0.035]
)

save_button = Button(
    save_axis,
    "Save Dashboard"
)


# ============================================================
# 17. SAVE DASHBOARD
# ============================================================

def save_dashboard(event):

    save_path = (
        output_dir /
        f"MRI_dashboard_X{x_index}_Y{y_index}_Z{z_index}.png"
    )

    fig.savefig(
        save_path,
        dpi=300,
        bbox_inches="tight"
    )

    print("\nDashboard saved!")

    print(
        "Output:",
        save_path
    )


save_button.on_clicked(
    save_dashboard
)


# ============================================================
# 18. INITIAL UPDATE
# ============================================================

update_dashboard()


# ============================================================
# 19. START DASHBOARD
# ============================================================

print("\n[3] DASHBOARD READY!")

print("\nControls:")

print(
    "• Move X, Y and Z sliders"
)

print(
    "• Click inside any MRI plane"
)

print(
    "• Inspect voxel intensity"
)

print(
    "• Inspect physical coordinates"
)

print(
    "• View intensity histogram"
)

print(
    "• Save dashboard snapshot"
)

print(
    "\nClose the window when finished."
)


plt.show()


# ============================================================
# FINAL
# ============================================================

print("\n" + "=" * 70)

print(
    "             MRI DASHBOARD CLOSED"
)

print("=" * 70)