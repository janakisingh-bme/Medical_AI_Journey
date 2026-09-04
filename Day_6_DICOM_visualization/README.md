# Day 6: DICOM Visualization

## What I Learned Today

- ✅ How to load and display DICOM images
- ✅ What Hounsfield Units are and their scale
- ✅ How window/level adjustments work
- ✅ Common CT window settings (lung, soft tissue, bone)
- ✅ How to fix missing transfer syntax errors
- ✅ How to extract and display metadata

## Key Concepts

### Hounsfield Units (HU)
- Air: -1000
- Fat: -100
- Water: 0
- Soft tissue: +40
- Bone: +400 to +1000

### Window/Level
- **Center (Level)**: Middle HU value to display
- **Width (Window)**: Range of HU values to show
- Formula: Lower = Center - Width/2, Upper = Center + Width/2

## Scripts Created

1. `01_basic_visualization.py` - Basic DICOM loading and display
2. `02_windowing_comparison.py` - Compare multiple window settings
3. `03_interactive_viewer.py` - Interactive window adjustment
4. `04_metadata_viewer.py` - Explore DICOM tags

## Common Window Settings

| Anatomy | Center | Width |
|---------|--------|-------|
| Lung | -600 | 1500 |
| Soft Tissue | 40 | 400 |
| Bone | 600 | 1500 |
| Brain | 40 | 80 |
| Liver | 30 | 150 |

## Challenges Faced

- Fixed ImportError with transfer syntax UIDs
- Learned about camelCase naming in pydicom
- Understood the difference between raw pixel values and HU

## Next Steps (Day 7)

- Learn NIfTI format
- Work with SimpleITK
- Start 3D visualization