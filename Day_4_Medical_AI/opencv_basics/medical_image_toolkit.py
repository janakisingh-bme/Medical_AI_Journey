import cv2
import os

# -----------------------------
# 1. Load image
# -----------------------------

image_path = "Day_4_Medical_AI/images/sample.png"

image = cv2.imread(image_path)

if image is None:
    print("Error: Image could not be loaded.")
    exit()

print("Image loaded successfully.")


# -----------------------------
# 2. Resize image
# -----------------------------

resized = cv2.resize(image, (224, 224))


# -----------------------------
# 3. Convert to grayscale
# -----------------------------

gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)


# -----------------------------
# 4. Gaussian Blur
# -----------------------------

blurred = cv2.GaussianBlur(gray, (5, 5), 0)


# -----------------------------
# 5. Canny Edge Detection
# -----------------------------

edges = cv2.Canny(blurred, 50, 150)


# -----------------------------
# 6. Thresholding
# -----------------------------

_, threshold = cv2.threshold(
    gray,
    127,
    255,
    cv2.THRESH_BINARY
)


# -----------------------------
# 7. Rotation
# -----------------------------

rotated = cv2.rotate(
    resized,
    cv2.ROTATE_90_CLOCKWISE
)


# -----------------------------
# 8. Flipping
# -----------------------------

flipped = cv2.flip(resized, 1)


# -----------------------------
# 9. Create output folder
# -----------------------------

output_folder = "Day_4_Medical_AI/outputs"

os.makedirs(output_folder, exist_ok=True)


# -----------------------------
# 10. Save processed images
# -----------------------------

cv2.imwrite(
    output_folder + "/resized.png",
    resized
)

cv2.imwrite(
    output_folder + "/grayscale.png",
    gray
)

cv2.imwrite(
    output_folder + "/blurred.png",
    blurred
)

cv2.imwrite(
    output_folder + "/edges.png",
    edges
)

cv2.imwrite(
    output_folder + "/threshold.png",
    threshold
)

cv2.imwrite(
    output_folder + "/rotated.png",
    rotated
)

cv2.imwrite(
    output_folder + "/flipped.png",
    flipped
)

print("All processed images saved successfully.")


# -----------------------------
# 11. Display results
# -----------------------------

cv2.imshow("Original X-Ray", image)
cv2.imshow("Resized", resized)
cv2.imshow("Grayscale", gray)
cv2.imshow("Gaussian Blur", blurred)
cv2.imshow("Canny Edges", edges)
cv2.imshow("Threshold", threshold)
cv2.imshow("Rotated", rotated)
cv2.imshow("Flipped", flipped)

cv2.waitKey(0)
cv2.destroyAllWindows()