# 🧠 Day 8 — 3D Medical Image Visualization

A hands-on Medical AI project focused on **3D visualization, interactive slice navigation, segmentation, surface extraction, and quantitative analysis of NIfTI brain MRI data** using Python.

---

## 📌 Project Overview

Medical images such as MRI scans are stored as 3D volumetric data rather than ordinary 2D images.

In this project, a T1-weighted brain MRI in **NIfTI (`.nii.gz`) format** is processed and visualized in multiple ways.

The project progresses from basic slice visualization to interactive 3D reconstruction and quantitative mesh analysis.

### Main Pipeline

```text
NIfTI Brain MRI
      ↓
SimpleITK
      ↓
NumPy 3D Volume
      ↓
Slice Visualization
      ↓
Axial / Coronal / Sagittal Views
      ↓
Interactive Navigation
      ↓
3D Volume Visualization
      ↓
Marching Cubes
      ↓
3D Surface Mesh
      ↓
Mesh Measurements
      ↓
Threshold Analysis
      ↓
MRI Analysis Dashboard