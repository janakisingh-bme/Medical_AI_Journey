import cv2

image = cv2.imread("Day_4_Medical_AI/images/sample.png")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite("Day_4_Medical_AI/outputs/grayscale.png", gray_image)

print("Grayscale image saved successfully")