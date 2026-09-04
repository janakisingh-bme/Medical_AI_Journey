"""
Day 6 - DICOM Visualization
01_basic_visualization.py

Basic visualization of a DICOM CT image:
  1. Load DICOM file (with transfer-syntax fix)
  2. Print key metadata
  3. Show image statistics
  4. Visualize: raw grayscale, windowed views, histogram
  5. Save all figures to ./outputs
"""

import os
import numpy as np
import pydicom
from pydicom.uid import (
    ImplicitVRLittleEndian,
    ExplicitVRLittleEndian,
    JPEGBaseline8Bit,
)
import matplotlib.pyplot as plt
from datetime import datetime


# ------------------------------------------------------------------
# Helper: fix missing Transfer Syntax UID
# ------------------------------------------------------------------
def ensure_transfer_syntax(ds):
    """
    Some DICOM files are missing the (0002,0010) Transfer Syntax UID
    tag. pydicom needs it to decode pixel data.
    We try the two common uncompressed encodings, then a common
    compressed one, until pixel_array works.
    """
    # Already present -> nothing to do
    if getattr(ds.file_meta, "TransferSyntaxUID", None) is not None:
        return

    candidates = [
        ImplicitVRLittleEndian,
        ExplicitVRLittleEndian,
        JPEGBaseline8Bit,          # in case it is JPEG-compressed
    ]

    for ts in candidates:
        ds.file_meta.TransferSyntaxUID = ts
        try:
            _ = ds.pixel_array        # test decode
            print(f"[OK] Transfer syntax set to: {ts.name}")
            return
        except Exception:
            continue

    raise RuntimeError(
        "Could not decode pixel data. "
        "The file may use a transfer syntax not listed in the candidates."
    )


# ------------------------------------------------------------------
# Helper: print key metadata
# ------------------------------------------------------------------
def print_metadata(ds):
    print("=" * 50)
    print("  DICOM METADATA")
    print("=" * 50)
    tags = [
        "PatientID",
        "PatientName",
        "PatientAge",
        "PatientSex",
        "StudyDate",
        "SeriesDate",
        "Modality",
        "SliceLocation",
        "InstanceNumber",
        "Rows",
        "Columns",
        "BitsAllocated",
        "PixelRepresentation",
        "RescaleIntercept",
        "RescaleSlope",
        "KVP",
        "SliceThickness",
    ]
    for tag in tags:
        value = ds.get(tag, "N/A")
        print(f"  {tag:<22s}: {value}")
    print("=" * 50)


# ------------------------------------------------------------------
# Helper: print image statistics
# ------------------------------------------------------------------
def print_stats(arr, label="Image"):
    print(f"\n--- {label} Statistics ---")
    print(f"  Shape           : {arr.shape}")
    print(f"  Dtype           : {arr.dtype}")
    print(f"  Min / Max       : {arr.min()} / {arr.max()}")
    print(f"  Mean            : {arr.mean():.2f}")
    print(f"  Std             : {arr.std():.2f}")
    print(f"  Median          : {np.median(arr):.2f}")
    print(f"  Percentiles 1/50/99 : "
          f"{np.percentile(arr, 1):.1f} / "
          f"{np.percentile(arr, 50):.1f} / "
          f"{np.percentile(arr, 99):.1f}")


# ------------------------------------------------------------------
# Helper: apply Hounsfield rescale (CT)
# ------------------------------------------------------------------
def to_hounsfield(ds):
    """Convert raw pixel values to Hounsfield Units (HU)."""
    arr = ds.pixel_array.astype(np.float64)
    slope     = float(ds.get("RescaleSlope", 1))
    intercept = float(ds.get("RescaleIntercept", 0))
    return arr * slope + intercept


# ------------------------------------------------------------------
# Helper: simple windowing
# ------------------------------------------------------------------
def apply_window(arr, center, width):
    """Clip and normalise to [0, 255] for display."""
    lower = center - width / 2.0
    upper = center + width / 2.0
    clipped = np.clip(arr, lower, upper)
    norm = (clipped - lower) / (upper - lower) * 255
    return norm.astype(np.uint8)


# ------------------------------------------------------------------
# MAIN
# ------------------------------------------------------------------
def main():
    # 1. Create folders
    os.makedirs("data", exist_ok=True)
    os.makedirs("outputs", exist_ok=True)

    # 2. Path to DICOM file
    dicom_path = "data/ct.dcm"

    if not os.path.exists(dicom_path):
        raise FileNotFoundError(
            f"File not found: {dicom_path}\n"
            "Place your CT DICOM file in the 'data/' folder."
        )

    # 3. Read DICOM
    print(f"Loading: {dicom_path}")
    ds = pydicom.dcmread(dicom_path)
    print("DICOM file loaded successfully!\n")

    # 4. *** FIX: ensure transfer syntax is present ***
    ensure_transfer_syntax(ds)

    # 5. Print metadata
    print_metadata(ds)

    # 6. Get pixel array
    raw_arr = ds.pixel_array
    print_stats(raw_arr, label="Raw Pixel Data")

    # 7. Convert to Hounsfield Units (CT only)
    if ds.get("Modality", "") == "CT":
        hu_arr = to_hounsfield(ds)
        print_stats(hu_arr, label="Hounsfield Units")
    else:
        hu_arr = raw_arr.astype(np.float64)

    # 8. Timestamp for output filenames
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")

    # ----------------------------------------------------------------
    # FIGURE 1 - Raw grayscale (no windowing)
    # ----------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.imshow(raw_arr, cmap="gray")
    ax.set_title("Raw Pixel Data (no windowing)")
    ax.axis("off")
    fig.tight_layout()
    fig.savefig(f"outputs/{ts}_01_raw.png", dpi=150)
    plt.show()

    # ----------------------------------------------------------------
    # FIGURE 2 - Three common CT windows (side by side)
    # ----------------------------------------------------------------
    windows = {
        "Lung  (C=-600, W=1500)":    (-600, 1500),
        "Soft Tissue (C=40, W=400)": (40, 400),
        "Bone  (C=600, W=1500)":     (600, 1500),
    }

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    for ax, (label, (c, w)) in zip(axes, windows.items()):
        win = apply_window(hu_arr, c, w)
        ax.imshow(win, cmap="gray")
        ax.set_title(label, fontsize=11)
        ax.axis("off")
    fig.suptitle("CT Windowing", fontsize=13)
    fig.tight_layout()
    fig.savefig(f"outputs/{ts}_02_windows.png", dpi=150)
    plt.show()

    # ----------------------------------------------------------------
    # FIGURE 3 - Histogram of Hounsfield values
    # ----------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.hist(hu_arr.ravel(), bins=256, range=(-1024, 1024),
            color="steelblue", edgecolor="none", alpha=0.85)
    # Mark common tissue HU values
    for hu, name in [(-1000, "Air"), (-50, "Fat"),
                     (0, "Water"), (40, "Soft Tissue"),
                     (100, "Muscle"), (700, "Bone")]:
        ax.axvline(hu, color="red", linestyle="--", linewidth=0.8)
        ax.text(hu, ax.get_ylim()[1] * 0.92, name,
                rotation=90, fontsize=7, color="red", va="top")
    ax.set_xlabel("Hounsfield Units (HU)")
    ax.set_ylabel("Pixel Count")
    ax.set_title("HU Histogram")
    fig.tight_layout()
    fig.savefig(f"outputs/{ts}_03_histogram.png", dpi=150)
    plt.show()

    # ----------------------------------------------------------------
    # FIGURE 4 - Side-by-side: raw vs soft-tissue window
    # ----------------------------------------------------------------
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    axes[0].imshow(raw_arr, cmap="gray")
    axes[0].set_title("Raw (0-255 mapped)")
    axes[0].axis("off")

    soft = apply_window(hu_arr, 40, 400)
    axes[1].imshow(soft, cmap="gray")
    axes[1].set_title("Soft-Tissue Window (C=40, W=400)")
    axes[1].axis("off")

    fig.tight_layout()
    fig.savefig(f"outputs/{ts}_04_raw_vs_window.png", dpi=150)
    plt.show()

    # ----------------------------------------------------------------
    # Save a copy of the image as PNG (soft-tissue window)
    # ----------------------------------------------------------------
    plt.imsave(f"outputs/{ts}_ct_soft_tissue.png",
               apply_window(hu_arr, 40, 400), cmap="gray")

    print(f"\nAll figures saved to: {os.path.abspath('outputs')}/")
    print("Done.")


if __name__ == "__main__":
    main()