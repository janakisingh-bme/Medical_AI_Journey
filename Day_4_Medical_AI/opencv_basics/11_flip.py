import cv2

image = cv2.imread("Day_4_Medical_AI/images/sample.png")

flipped_image = cv2.flip(image, 1)

cv2.imshow("Original X-Ray", image)
cv2.imshow("Flipped X-Ray", flipped_image)

cv2.waitKey(0)
cv2.destroyAllWindows()