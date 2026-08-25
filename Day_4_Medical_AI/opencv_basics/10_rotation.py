import cv2

image = cv2.imread("Day_4_Medical_AI/images/sample.png")

rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

cv2.imshow("Original X-Ray", image)
cv2.imshow("Rotated X-Ray", rotated_image)

cv2.waitKey(0)
cv2.destroyAllWindows()