import SimpleITK as sitk
import numpy as np
import plotly.graph_objects as go
from skimage.measure import marching_cubes
from pathlib import Path


# ============================================================
# 1. PROJECT PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

input_path = BASE_DIR / "data" / "brain_T1w.nii.gz"
output_dir = BASE_DIR / "outputs"

output_dir.mkdir(exist_ok=True)

output_path = output_dir / "brain_surface.html"


# ============================================================
# 2. LOAD MRI
# ============================================================

print("=" * 70)
print("             3D BRAIN SURFACE EXTRACTION")
print("=" * 70)

print("\n[1] Loading MRI...")

image = sitk.ReadImage(str(input_path))

# Standardize orientation
image = sitk.DICOMOrient(image, "LPS")

volume = sitk.GetArrayFromImage(image)

print("MRI loaded successfully!")
print("Volume shape:", volume.shape)


# ============================================================
# 3. CONVERT TO FLOAT
# ============================================================

volume = volume.astype(np.float32)


# ============================================================
# 4. NORMALIZE
# ============================================================

print("\n[2] Normalizing intensity...")

minimum = volume.min()
maximum = volume.max()

normalized = (
    volume - minimum
) / (
    maximum - minimum
)

print("Minimum:", minimum)
print("Maximum:", maximum)


# ============================================================
# 5. SMOOTH VOLUME
# ============================================================

print("\n[3] Smoothing volume...")

from scipy.ndimage import gaussian_filter

smoothed = gaussian_filter(
    normalized,
    sigma=1
)

print("Smoothing complete.")


# ============================================================
# 6. CHOOSE SURFACE LEVEL
# ============================================================

level = 0.20

print("\n[4] Marching Cubes")

print("Surface threshold:", level)


# ============================================================
# 7. EXTRACT SURFACE
# ============================================================

print("\nExtracting 3D surface...")

vertices, faces, normals, values = marching_cubes(
    smoothed,
    level=level
)

print("Surface extraction complete!")


# ============================================================
# 8. DISPLAY MESH INFORMATION
# ============================================================

print("\n[5] MESH INFORMATION")

print("Vertices:", len(vertices))
print("Faces:", len(faces))

print("Vertex shape:", vertices.shape)
print("Face shape:", faces.shape)


# ============================================================
# 9. SEPARATE COORDINATES
# ============================================================

z = vertices[:, 0]
y = vertices[:, 1]
x = vertices[:, 2]


# ============================================================
# 10. CREATE 3D MESH
# ============================================================

print("\n[6] Creating interactive 3D mesh...")

mesh = go.Mesh3d(

    x=x,
    y=y,
    z=z,

    i=faces[:, 0],
    j=faces[:, 1],
    k=faces[:, 2],

    intensity=values,

    colorscale="Gray",

    opacity=0.85,

    flatshading=False,

    name="Brain Surface"
)


# ============================================================
# 11. CREATE FIGURE
# ============================================================

fig = go.Figure(
    data=[mesh]
)


# ============================================================
# 12. CONFIGURE 3D SCENE
# ============================================================

fig.update_layout(

    title="3D Brain Surface - Marching Cubes",

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
# 13. SAVE HTML
# ============================================================

print("\n[7] Saving 3D surface...")

fig.write_html(
    str(output_path)
)

print("Saved successfully!")

print("\nOutput:")
print(output_path)


# ============================================================
# 14. OPEN VIEWER
# ============================================================

print("\n[8] Opening interactive viewer...")

fig.show()


# ============================================================
# FINAL
# ============================================================

print("\n" + "=" * 70)
print("             3D SURFACE COMPLETE")
print("=" * 70)

print("\nMesh statistics:")
print("Vertices:", len(vertices))
print("Faces:", len(faces))

print("\nGenerated file:")
print("outputs/brain_surface.html")