import SimpleITK as sitk

# Read NIfTI image
image = sitk.ReadImage("data/minimal.nii")

print("NIfTI image loaded successfully!")
print("Image size:", image.GetSize())
print("Image spacing:", image.GetSpacing())
print("Pixel type:", image.GetPixelIDTypeAsString())