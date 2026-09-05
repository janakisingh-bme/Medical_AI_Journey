import SimpleITK as sitk
import matplotlib.pyplot as plt


# ==========================================
# 1. LOAD NIFTI IMAGE
# ==========================================

image = sitk.ReadImage("data/brain_T1w.nii.gz")


# ==========================================
# 2. CONVERT TO NUMPY ARRAY
# ==========================================

volume = sitk.GetArrayFromImage(image)


# ==========================================
# 3. DISPLAY VOLUME INFORMATION
# ==========================================

print("Volume shape:", volume.shape)
print("Number of dimensions:", volume.ndim)


# ==========================================
# 4. SELECT MIDDLE SLICE
# ==========================================

middle_slice = volume.shape[0] // 2

print("Total slices:", volume.shape[0])
print("Middle slice:", middle_slice)


# ==========================================
# 5. DISPLAY SLICE
# ==========================================

plt.figure(figsize=(6, 6))

plt.imshow(
    volume[middle_slice],
    cmap="gray"
)

plt.title(f"Middle Slice - {middle_slice}")
plt.axis("off")

plt.show()