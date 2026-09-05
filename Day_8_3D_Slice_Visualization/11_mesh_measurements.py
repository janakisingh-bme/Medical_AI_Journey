import SimpleITK as sitk
import numpy as np
from scipy.ndimage import gaussian_filter
from skimage.measure import marching_cubes
from pathlib import Path


# ============================================================
# 1. PROJECT PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

input_path = BASE_DIR / "data" / "brain_T1w.nii.gz"
output_dir = BASE_DIR / "outputs"

output_dir.mkdir(exist_ok=True)

report_path = output_dir / "mesh_measurements.txt"


# ============================================================
# 2. LOAD MRI
# ============================================================

print("=" * 70)
print("              3D BRAIN MESH MEASUREMENTS")
print("=" * 70)

print("\n[1] Loading MRI...")

image = sitk.ReadImage(str(input_path))

# Standardize orientation
image = sitk.DICOMOrient(image, "LPS")

volume = sitk.GetArrayFromImage(
    image
).astype(np.float32)

print("MRI loaded successfully!")


# ============================================================
# 3. VOXEL SPACING
# ============================================================

spacing_x, spacing_y, spacing_z = image.GetSpacing()

print("\n[2] VOXEL SPACING")

print(f"X: {spacing_x:.3f} mm")
print(f"Y: {spacing_y:.3f} mm")
print(f"Z: {spacing_z:.3f} mm")


# ============================================================
# 4. NORMALIZE MRI
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
# 5. SMOOTH
# ============================================================

print("\n[4] SMOOTHING MRI...")

smoothed = gaussian_filter(
    normalized,
    sigma=1
)

print("Smoothing complete.")


# ============================================================
# 6. MARCHING CUBES
# ============================================================

threshold = 0.20

print("\n[5] EXTRACTING 3D SURFACE")

print("Threshold:", threshold)

vertices, faces, normals, values = marching_cubes(
    smoothed,
    level=threshold,
    spacing=(
        spacing_z,
        spacing_y,
        spacing_x
    )
)

print("Surface extracted successfully!")


# ============================================================
# 7. BASIC MESH STATISTICS
# ============================================================

num_vertices = len(vertices)
num_faces = len(faces)

print("\n[6] MESH STATISTICS")

print("Vertices:", num_vertices)
print("Faces:", num_faces)


# ============================================================
# 8. PHYSICAL DIMENSIONS
# ============================================================

z_coordinates = vertices[:, 0]
y_coordinates = vertices[:, 1]
x_coordinates = vertices[:, 2]

x_min = x_coordinates.min()
x_max = x_coordinates.max()

y_min = y_coordinates.min()
y_max = y_coordinates.max()

z_min = z_coordinates.min()
z_max = z_coordinates.max()

x_dimension = x_max - x_min
y_dimension = y_max - y_min
z_dimension = z_max - z_min


print("\n[7] PHYSICAL DIMENSIONS")

print(f"X dimension: {x_dimension:.2f} mm")
print(f"Y dimension: {y_dimension:.2f} mm")
print(f"Z dimension: {z_dimension:.2f} mm")


# ============================================================
# 9. CALCULATE TRIANGLE AREAS
# ============================================================

print("\n[8] CALCULATING SURFACE AREA...")

# Get the three vertices of every triangle

triangle_vertices = vertices[faces]

v1 = triangle_vertices[:, 0, :]
v2 = triangle_vertices[:, 1, :]
v3 = triangle_vertices[:, 2, :]

# Calculate two edges

edge1 = v2 - v1
edge2 = v3 - v1

# Cross product

cross_product = np.cross(
    edge1,
    edge2
)

# Triangle area = 0.5 * magnitude of cross product

triangle_areas = (
    0.5 *
    np.linalg.norm(
        cross_product,
        axis=1
    )
)

surface_area = triangle_areas.sum()


print(
    f"Surface area: "
    f"{surface_area:.2f} mm²"
)


# ============================================================
# 10. CALCULATE MESH VOLUME
# ============================================================

print("\n[9] CALCULATING MESH VOLUME...")

# Signed tetrahedron volume for each triangle
# relative to the origin

cross = np.cross(
    v2,
    v3
)

tetra_volumes = np.einsum(
    "ij,ij->i",
    v1,
    cross
) / 6.0

mesh_volume = abs(
    tetra_volumes.sum()
)


print(
    f"Mesh volume: "
    f"{mesh_volume:.2f} mm³"
)


# ============================================================
# 11. CONVERT VOLUME TO CM³
# ============================================================

volume_cm3 = (
    mesh_volume / 1000
)


print(
    f"Mesh volume: "
    f"{volume_cm3:.2f} cm³"
)


# ============================================================
# 12. CREATE REPORT
# ============================================================

report = f"""
============================================================
              3D BRAIN MESH MEASUREMENT REPORT
============================================================

INPUT
------------------------------------------------------------
File: {input_path.name}

MRI Volume Shape:
{volume.shape}

Voxel Spacing:
X = {spacing_x:.3f} mm
Y = {spacing_y:.3f} mm
Z = {spacing_z:.3f} mm


SEGMENTATION
------------------------------------------------------------
Intensity Threshold:
{threshold:.2f}

Gaussian Smoothing:
sigma = 1


MESH STATISTICS
------------------------------------------------------------
Vertices:
{num_vertices}

Faces:
{num_faces}


PHYSICAL DIMENSIONS
------------------------------------------------------------
X Dimension:
{x_dimension:.2f} mm

Y Dimension:
{y_dimension:.2f} mm

Z Dimension:
{z_dimension:.2f} mm


SURFACE MEASUREMENTS
------------------------------------------------------------
Surface Area:
{surface_area:.2f} mm²


VOLUME MEASUREMENTS
------------------------------------------------------------
Mesh Volume:
{mesh_volume:.2f} mm³

Mesh Volume:
{volume_cm3:.2f} cm³


============================================================
                    END OF REPORT
============================================================
"""


# ============================================================
# 13. SAVE REPORT
# ============================================================

with open(
    report_path,
    "w",
    encoding="utf-8"
) as file:

    file.write(report)


# ============================================================
# 14. DISPLAY REPORT
# ============================================================

print("\n" + report)

print("Report saved to:")
print(report_path)


# ============================================================
# FINAL
# ============================================================

print("\n" + "=" * 70)
print("              MEASUREMENT COMPLETE")
print("=" * 70)