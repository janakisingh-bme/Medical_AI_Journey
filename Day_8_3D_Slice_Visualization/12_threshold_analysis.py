import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt

from scipy.ndimage import gaussian_filter
from skimage.measure import marching_cubes

from pathlib import Path
import csv


# ============================================================
# 1. PROJECT PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

input_path = BASE_DIR / "data" / "brain_T1w.nii.gz"
output_dir = BASE_DIR / "outputs"

output_dir.mkdir(exist_ok=True)

csv_path = output_dir / "threshold_analysis.csv"

volume_plot_path = output_dir / "threshold_vs_volume.png"

surface_plot_path = output_dir / "threshold_vs_surface_area.png"


# ============================================================
# 2. LOAD MRI
# ============================================================

print("=" * 70)
print("             MRI THRESHOLD ANALYSIS")
print("=" * 70)

print("\n[1] Loading MRI...")

if not input_path.exists():

    raise FileNotFoundError(
        f"\nMRI file not found:\n{input_path}"
    )


image = sitk.ReadImage(
    str(input_path)
)

# Standardize orientation
image = sitk.DICOMOrient(
    image,
    "LPS"
)

volume = sitk.GetArrayFromImage(
    image
).astype(np.float32)


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

print("\n[3] NORMALIZING MRI...")

minimum = volume.min()
maximum = volume.max()

if maximum == minimum:

    raise ValueError(
        "MRI has constant intensity values."
    )


normalized = (
    volume - minimum
) / (
    maximum - minimum
)


print("Normalization complete.")

print(
    f"Normalized range: "
    f"{normalized.min():.2f} - "
    f"{normalized.max():.2f}"
)


# ============================================================
# 5. SMOOTH MRI
# ============================================================

print("\n[4] APPLYING GAUSSIAN SMOOTHING...")

smoothed = gaussian_filter(
    normalized,
    sigma=1
)

print("Smoothing complete.")


# ============================================================
# 6. THRESHOLDS TO TEST
# ============================================================

thresholds = [
    0.10,
    0.15,
    0.20,
    0.25,
    0.30,
    0.35,
    0.40
]


print("\n[5] THRESHOLD ANALYSIS")

print(
    "Testing thresholds:",
    thresholds
)


# ============================================================
# 7. RESULT STORAGE
# ============================================================

results = []


# ============================================================
# 8. PROCESS EACH THRESHOLD
# ============================================================

for threshold in thresholds:

    print("\n" + "-" * 70)

    print(
        f"Processing threshold: {threshold:.2f}"
    )

    try:

        # ----------------------------------------------------
        # Marching Cubes
        # ----------------------------------------------------

        vertices, faces, normals, values = marching_cubes(

            smoothed,

            level=threshold,

            spacing=(
                spacing_z,
                spacing_y,
                spacing_x
            )
        )


        # ----------------------------------------------------
        # Number of vertices and faces
        # ----------------------------------------------------

        num_vertices = len(vertices)

        num_faces = len(faces)


        # ----------------------------------------------------
        # Get triangle vertices
        # ----------------------------------------------------

        triangle_vertices = vertices[faces]

        v1 = triangle_vertices[:, 0, :]
        v2 = triangle_vertices[:, 1, :]
        v3 = triangle_vertices[:, 2, :]


        # ----------------------------------------------------
        # Calculate triangle areas
        # ----------------------------------------------------

        edge1 = v2 - v1

        edge2 = v3 - v1

        cross_product = np.cross(
            edge1,
            edge2
        )

        triangle_areas = (
            0.5 *
            np.linalg.norm(
                cross_product,
                axis=1
            )
        )

        surface_area = (
            triangle_areas.sum()
        )


        # ----------------------------------------------------
        # Calculate mesh volume
        # ----------------------------------------------------

        cross = np.cross(
            v2,
            v3
        )

        tetra_volumes = (
            np.einsum(
                "ij,ij->i",
                v1,
                cross
            )
            / 6.0
        )

        mesh_volume = abs(
            tetra_volumes.sum()
        )


        # ----------------------------------------------------
        # Convert mm³ → cm³
        # ----------------------------------------------------

        volume_cm3 = (
            mesh_volume / 1000
        )


        # ----------------------------------------------------
        # Store results
        # ----------------------------------------------------

        results.append({

            "threshold": threshold,

            "vertices": num_vertices,

            "faces": num_faces,

            "surface_area_mm2": surface_area,

            "volume_mm3": mesh_volume,

            "volume_cm3": volume_cm3

        })


        # ----------------------------------------------------
        # Print results
        # ----------------------------------------------------

        print(
            f"Vertices      : {num_vertices:,}"
        )

        print(
            f"Faces         : {num_faces:,}"
        )

        print(
            f"Surface area  : "
            f"{surface_area:,.2f} mm²"
        )

        print(
            f"Volume        : "
            f"{mesh_volume:,.2f} mm³"
        )

        print(
            f"Volume        : "
            f"{volume_cm3:,.2f} cm³"
        )


    except ValueError:

        print(
            f"No valid surface found "
            f"at threshold {threshold:.2f}"
        )


# ============================================================
# 9. CHECK RESULTS
# ============================================================

if len(results) == 0:

    raise RuntimeError(
        "No valid surfaces were generated."
    )


# ============================================================
# 10. SAVE CSV
# ============================================================

print("\n[6] SAVING RESULTS TO CSV...")

with open(
    csv_path,
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.DictWriter(

        file,

        fieldnames=[
            "threshold",
            "vertices",
            "faces",
            "surface_area_mm2",
            "volume_mm3",
            "volume_cm3"
        ]
    )

    writer.writeheader()

    writer.writerows(
        results
    )


print("CSV saved successfully!")

print(
    "Output:",
    csv_path
)


# ============================================================
# 11. EXTRACT RESULTS FOR PLOTTING
# ============================================================

threshold_values = [
    item["threshold"]
    for item in results
]

volume_values = [
    item["volume_cm3"]
    for item in results
]

surface_values = [
    item["surface_area_mm2"]
    for item in results
]


# ============================================================
# 12. PRINT SUMMARY TABLE
# ============================================================

print("\n[7] SUMMARY")

print()

print(
    f"{'Threshold':<12}"
    f"{'Vertices':<15}"
    f"{'Faces':<15}"
    f"{'Surface mm²':<20}"
    f"{'Volume cm³':<15}"
)

print("-" * 75)


for item in results:

    print(

        f"{item['threshold']:<12.2f}"

        f"{item['vertices']:<15,}"

        f"{item['faces']:<15,}"

        f"{item['surface_area_mm2']:<20,.2f}"

        f"{item['volume_cm3']:<15,.2f}"
    )


# ============================================================
# 13. THRESHOLD VS VOLUME
# ============================================================

print("\n[8] CREATING VOLUME GRAPH...")

plt.figure(
    figsize=(8, 5)
)

plt.plot(
    threshold_values,
    volume_values,
    marker="o"
)

plt.xlabel(
    "Intensity Threshold"
)

plt.ylabel(
    "Mesh Volume (cm³)"
)

plt.title(
    "Threshold vs 3D Mesh Volume"
)

plt.grid(
    True
)

plt.tight_layout()

plt.savefig(
    volume_plot_path,
    dpi=300
)

plt.show()


print(
    "Volume graph saved:"
)

print(
    volume_plot_path
)


# ============================================================
# 14. THRESHOLD VS SURFACE AREA
# ============================================================

print("\n[9] CREATING SURFACE AREA GRAPH...")

plt.figure(
    figsize=(8, 5)
)

plt.plot(
    threshold_values,
    surface_values,
    marker="o"
)

plt.xlabel(
    "Intensity Threshold"
)

plt.ylabel(
    "Surface Area (mm²)"
)

plt.title(
    "Threshold vs 3D Mesh Surface Area"
)

plt.grid(
    True
)

plt.tight_layout()

plt.savefig(
    surface_plot_path,
    dpi=300
)

plt.show()


print(
    "Surface area graph saved:"
)

print(
    surface_plot_path
)


# ============================================================
# 15. FIND LARGEST VOLUME
# ============================================================

largest_volume = max(
    results,
    key=lambda x: x["volume_cm3"]
)


print("\n[10] LARGEST MEASURED VOLUME")

print(
    f"Threshold: "
    f"{largest_volume['threshold']:.2f}"
)

print(
    f"Volume: "
    f"{largest_volume['volume_cm3']:,.2f} cm³"
)


# ============================================================
# 16. FINAL SUMMARY
# ============================================================

print("\n" + "=" * 70)

print(
    "             THRESHOLD ANALYSIS COMPLETE"
)

print("=" * 70)

print("\nGenerated files:")

print(
    "1.",
    csv_path
)

print(
    "2.",
    volume_plot_path
)

print(
    "3.",
    surface_plot_path
)

print("\nThresholds analyzed:")

for threshold in threshold_values:

    print(
        f"   • {threshold:.2f}"
    )

print("\nDone! 🧠📊")