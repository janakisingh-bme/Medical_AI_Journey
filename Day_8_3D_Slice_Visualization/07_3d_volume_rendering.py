import SimpleITK as sitk
import numpy as np
import plotly.graph_objects as go
from pathlib import Path


# ============================================================
# 1. PROJECT PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

input_path = BASE_DIR / "data" / "brain_T1w.nii.gz"
output_dir = BASE_DIR / "outputs"

output_dir.mkdir(exist_ok=True)

output_path = output_dir / "brain_3d_visualization.html"


# ============================================================
# 2. LOAD MRI
# ============================================================

print("=" * 65)
print("              3D BRAIN MRI VISUALIZATION")
print("=" * 65)

print("\n[1] Loading MRI...")

image = sitk.ReadImage(str(input_path))

# Standard anatomical orientation
image = sitk.DICOMOrient(image, "LPS")

volume = sitk.GetArrayFromImage(image)

print("MRI loaded successfully!")


# ============================================================
# 3. VOLUME INFORMATION
# ============================================================

print("\n[2] VOLUME INFORMATION")

print("Shape:", volume.shape)
print("Dimensions:", volume.ndim)
print("Data type:", volume.dtype)
print("Minimum intensity:", volume.min())
print("Maximum intensity:", volume.max())


# ============================================================
# 4. NORMALIZE INTENSITY
# ============================================================

print("\n[3] NORMALIZING INTENSITY...")

volume = volume.astype(np.float32)

minimum = volume.min()
maximum = volume.max()

normalized = (
    (volume - minimum)
    / (maximum - minimum)
)

print("Normalization complete.")


# ============================================================
# 5. REMOVE VERY DARK BACKGROUND
# ============================================================

print("\n[4] EXTRACTING BRAIN REGION...")

threshold = 0.20

mask = normalized > threshold

print("Threshold:", threshold)
print("Selected voxels:", np.sum(mask))


# ============================================================
# 6. GET VOXEL COORDINATES
# ============================================================

z, y, x = np.where(mask)

intensity = normalized[mask]

print("\n[5] 3D POINT CLOUD")

print("Number of points:", len(x))


# ============================================================
# 7. REDUCE POINTS
# ============================================================

# Very large MRI volumes can contain millions of voxels.
# Sampling makes the interactive viewer much faster.

max_points = 100000

if len(x) > max_points:

    print("\nLarge volume detected.")
    print("Reducing points for interactive visualization...")

    rng = np.random.default_rng(42)

    indices = rng.choice(
        len(x),
        max_points,
        replace=False
    )

    x = x[indices]
    y = y[indices]
    z = z[indices]

    intensity = intensity[indices]

print("Final points:", len(x))


# ============================================================
# 8. CREATE 3D SCATTER
# ============================================================

print("\n[6] CREATING 3D VISUALIZATION...")

fig = go.Figure(
    data=[
        go.Scatter3d(
            x=x,
            y=y,
            z=z,

            mode="markers",

            marker=dict(
                size=1.5,
                color=intensity,
                colorscale="Gray",
                opacity=0.35,
                colorbar=dict(
                    title="Intensity"
                )
            )
        )
    ]
)


# ============================================================
# 9. LAYOUT
# ============================================================

fig.update_layout(

    title="Interactive 3D Brain MRI",

    scene=dict(

        xaxis_title="X",
        yaxis_title="Y",
        zaxis_title="Z",

        aspectmode="data"
    ),

    width=1000,
    height=800
)


# ============================================================
# 10. SAVE HTML
# ============================================================

print("\n[7] SAVING 3D MODEL...")

fig.write_html(
    str(output_path)
)

print("3D visualization saved!")

print("Output:")
print(output_path)


# ============================================================
# 11. OPEN VISUALIZATION
# ============================================================

print("\n[8] OPENING 3D VIEWER...")

fig.show()


# ============================================================
# FINAL
# ============================================================

print("\n" + "=" * 65)
print("                 3D VISUALIZATION COMPLETE")
print("=" * 65)

print("\nYou can:")
print("  • Rotate the brain")
print("  • Zoom in/out")
print("  • Pan around")
print("  • Inspect intensity distribution")

print("\nGenerated:")
print("outputs/brain_3d_visualization.html")