import cv2

image = cv2.imread("Day_4_Medical_AI/images/sample.png")

if image is None:
    print("Image could not be loaded")
else:
    print("Image loaded successfully")