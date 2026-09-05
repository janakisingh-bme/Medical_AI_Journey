import SimpleITK as sitk
import numpy as np
import plotly.graph_objects as go
from skimage.measure import marching_cubes
from scipy.ndimage import gaussian_filter
from pathlib import Path


# ============================================================
# 1. PROJECT PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

input_path = BASE_DIR / "data" / "brain_T1w.nii.gz"
output_dir = BASE_DIR / "outputs"

output_dir.mkdir(exist_ok=True)

output_path = output_dir / "interactive_brain_segmentation.html"


# ============================================================
# 2. LOAD MRI
# ============================================================

print("=" * 70)
print("        INTERACTIVE 3D BRAIN SEGMENTATION")
print("=" * 70)

print("\n[1] Loading MRI...")

image = sitk.ReadImage(str(input_path))

# Standard orientation
image = sitk.DICOMOrient(image, "LPS")

volume = sitk.GetArrayFromImage(image).astype(np.float32)

print("MRI loaded successfully!")
print("Volume shape:", volume.shape)


# ============================================================
# 3. VOXEL SPACING
# ============================================================

spacing_x, spacing_y, spacing_z = image.GetSpacing()

print("\n[2] VOXEL SPACING")

print(f"X: {spacing_x:.3f} mm")
print(f"Y: {spacing_y:.3f} mm")
print(f"Z: {spacing_z:.3f} mm")


# ============================================================
# 4. NORMALIZE
# ============================================================

print("\n[3] NORMALIZING...")

minimum = volume.min()
maximum = volume.max()

normalized = (
    volume - minimum
) / (
    maximum - minimum
)

print("Normalization complete.")


# ============================================================
# 5. SMOOTH
# ============================================================

print("\n[4] SMOOTHING...")

smoothed = gaussian_filter(
    normalized,
    sigma=1
)

print("Smoothing complete.")


# ============================================================
# 6. CREATE MULTIPLE THRESHOLD SURFACES
# ============================================================

thresholds = [
    0.15,
    0.20,
    0.25,
    0.30,
    0.35,
    0.40
]

print("\n[5] GENERATING SURFACES")

fig = go.Figure()

for threshold in thresholds:

    print(f"Processing threshold: {threshold}")

    try:

        vertices, faces, normals, values = marching_cubes(
            smoothed,
            level=threshold,
            spacing=(
                spacing_z,
                spacing_y,
                spacing_x
            )
        )

        z = vertices[:, 0]
        y = vertices[:, 1]
        x = vertices[:, 2]

        fig.add_trace(

            go.Mesh3d(

                x=x,
                y=y,
                z=z,

                i=faces[:, 0],
                j=faces[:, 1],
                k=faces[:, 2],

                intensity=values,

                colorscale="Gray",

                opacity=0.90,

                visible=False,

                name=f"Threshold {threshold}"
            )
        )

    except ValueError:

        print(
            f"No surface found at threshold {threshold}"
        )


# ============================================================
# 7. SHOW FIRST VALID SURFACE
# ============================================================

if len(fig.data) == 0:

    raise RuntimeError(
        "No surface could be extracted."
    )

fig.data[0].visible = True


# ============================================================
# 8. CREATE SLIDER
# ============================================================

steps = []

for i, trace in enumerate(fig.data):

    visibility = [
        False
    ] * len(fig.data)

    visibility[i] = True

    threshold_value = thresholds[i]

    steps.append(

        dict(

            method="update",

            args=[
                {
                    "visible": visibility
                },
                {
                    "title":
                    f"3D Brain Surface - "
                    f"Threshold {threshold_value:.2f}"
                }
            ],

            label=f"{threshold_value:.2f}"
        )
    )


slider = [

    dict(

        active=0,

        currentvalue={
            "prefix": "Threshold: "
        },

        pad={
            "t": 50
        },

        steps=steps
    )
]


# ============================================================
# 9. LAYOUT
# ============================================================

fig.update_layout(

    title="3D Brain Surface - Threshold 0.15",

    sliders=slider,

    scene=dict(

        xaxis_title="X (mm)",
        yaxis_title="Y (mm)",
        zaxis_title="Z (mm)",

        aspectmode="data"
    ),

    width=1000,
    height=800
)


# ============================================================
# 10. SAVE
# ============================================================

print("\n[6] SAVING INTERACTIVE MODEL...")

fig.write_html(
    str(output_path)
)

print("Saved successfully!")

print("\nOutput:")
print(output_path)


# ============================================================
# 11. OPEN
# ============================================================

print("\n[7] Opening browser...")

fig.show()


# ============================================================
# FINAL
# ============================================================

print("\n" + "=" * 70)
print("          INTERACTIVE SEGMENTATION COMPLETE")
print("=" * 70)

print("\nAvailable thresholds:")

for threshold in thresholds:
    print(f"  {threshold:.2f}")

print("\nGenerated:")
print("outputs/interactive_brain_segmentation.html")