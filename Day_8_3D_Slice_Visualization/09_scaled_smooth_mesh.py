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

output_path = output_dir / "brain_scaled_mesh.html"


# ============================================================
# 2. LOAD MRI
# ============================================================

print("=" * 70)
print("          PHYSICALLY SCALED 3D BRAIN MESH")
print("=" * 70)

print("\n[1] Loading MRI...")

image = sitk.ReadImage(str(input_path))

# Standardize orientation
image = sitk.DICOMOrient(image, "LPS")

volume = sitk.GetArrayFromImage(image).astype(np.float32)

print("MRI loaded successfully!")


# ============================================================
# 3. GET VOXEL SPACING
# ============================================================

spacing_x, spacing_y, spacing_z = image.GetSpacing()

print("\n[2] VOXEL SPACING")

print(f"X spacing: {spacing_x:.3f} mm")
print(f"Y spacing: {spacing_y:.3f} mm")
print(f"Z spacing: {spacing_z:.3f} mm")


# ============================================================
# 4. NORMALIZE
# ============================================================

print("\n[3] NORMALIZING MRI...")

minimum = volume.min()
maximum = volume.max()

normalized = (
    volume - minimum
) / (
    maximum - minimum
)

print("Normalization complete.")


# ============================================================
# 5. SMOOTH VOLUME
# ============================================================

print("\n[4] SMOOTHING VOLUME...")

smoothed = gaussian_filter(
    normalized,
    sigma=1
)

print("Gaussian smoothing complete.")


# ============================================================
# 6. MARCHING CUBES
# ============================================================

threshold = 0.20

print("\n[5] EXTRACTING SURFACE")

print("Threshold:", threshold)

vertices, faces, normals, values = marching_cubes(
    smoothed,
    level=threshold,
    spacing=(spacing_z, spacing_y, spacing_x)
)

print("Surface extraction complete!")


# ============================================================
# 7. MESH INFORMATION
# ============================================================

print("\n[6] MESH INFORMATION")

print("Vertices:", len(vertices))
print("Faces:", len(faces))

print("\nPhysical coordinate ranges:")

print(
    "Z:",
    round(vertices[:, 0].min(), 2),
    "to",
    round(vertices[:, 0].max(), 2),
    "mm"
)

print(
    "Y:",
    round(vertices[:, 1].min(), 2),
    "to",
    round(vertices[:, 1].max(), 2),
    "mm"
)

print(
    "X:",
    round(vertices[:, 2].min(), 2),
    "to",
    round(vertices[:, 2].max(), 2),
    "mm"
)


# ============================================================
# 8. SEPARATE COORDINATES
# ============================================================

z = vertices[:, 0]
y = vertices[:, 1]
x = vertices[:, 2]


# ============================================================
# 9. CREATE 3D MESH
# ============================================================

print("\n[7] CREATING 3D MESH...")

mesh = go.Mesh3d(

    x=x,
    y=y,
    z=z,

    i=faces[:, 0],
    j=faces[:, 1],
    k=faces[:, 2],

    intensity=values,

    colorscale="Gray",

    opacity=0.90,

    flatshading=False,

    name="Brain Surface"
)


# ============================================================
# 10. CREATE FIGURE
# ============================================================

fig = go.Figure(
    data=[mesh]
)


# ============================================================
# 11. 3D SCENE
# ============================================================

fig.update_layout(

    title="Physically Scaled 3D Brain Surface",

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
# 12. SAVE
# ============================================================

print("\n[8] SAVING MODEL...")

fig.write_html(
    str(output_path)
)

print("3D model saved successfully!")

print("\nOutput:")
print(output_path)


# ============================================================
# 13. DISPLAY
# ============================================================

print("\n[9] OPENING VIEWER...")

fig.show()


# ============================================================
# FINAL SUMMARY
# ============================================================

print("\n" + "=" * 70)
print("                 MESH COMPLETE")
print("=" * 70)

print("\nMRI volume:", volume.shape)

print(
    f"Voxel spacing: "
    f"{spacing_x:.3f} × "
    f"{spacing_y:.3f} × "
    f"{spacing_z:.3f} mm"
)

print("Vertices:", len(vertices))
print("Faces:", len(faces))

print("\nGenerated file:")
print("outputs/brain_scaled_mesh.html")