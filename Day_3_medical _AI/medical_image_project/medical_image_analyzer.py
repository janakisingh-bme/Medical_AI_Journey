import numpy as np
import matplotlib.pyplot as plt


# --------------------------------
# 1. Create a medical image
# --------------------------------

image = np.array([
    [20, 30, 40, 50, 60],
    [30, 50, 80, 100, 70],
    [40, 80, 150, 180, 90],
    [30, 70, 120, 160, 80],
    [20, 40, 60, 80, 50]
])

print("Original Medical Image:")
print(image)


# --------------------------------
# 2. Image properties
# --------------------------------

print("\nImage Shape:", image.shape)
print("Number of Pixels:", image.size)


# --------------------------------
# 3. Indexing
# --------------------------------

pixel = image[2, 2]

print("\nPixel at row 3, column 3:", pixel)


# --------------------------------
# 4. Slicing
# --------------------------------

region = image[1:4, 1:4]

print("\nCentral Region:")
print(region)


# --------------------------------
# 5. Broadcasting
# --------------------------------

brighter_image = image + 30

print("\nBrighter Image:")
print(brighter_image)


# --------------------------------
# 6. Statistics
# --------------------------------

print("\nImage Statistics:")
print("Mean:", np.mean(image))
print("Maximum:", np.max(image))
print("Minimum:", np.min(image))
print("Standard Deviation:", np.std(image))


# --------------------------------
# 7. Matrix operation
# --------------------------------

enhanced_image = image * 1.5

print("\nEnhanced Image:")
print(enhanced_image)


# --------------------------------
# 8. Display Original Image
# --------------------------------

plt.figure()

plt.imshow(image, cmap="gray")

plt.title("Original Medical Image")
plt.xlabel("Pixels")
plt.ylabel("Pixels")

plt.colorbar(label="Pixel Intensity")

plt.show()


# --------------------------------
# 9. Display Brighter Image
# --------------------------------

plt.figure()

plt.imshow(brighter_image, cmap="gray")

plt.title("Brighter Medical Image")
plt.xlabel("Pixels")
plt.ylabel("Pixels")

plt.colorbar(label="Pixel Intensity")

plt.show()