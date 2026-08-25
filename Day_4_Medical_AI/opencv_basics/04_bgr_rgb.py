import cv2

image = cv2.imread("Day_4_Medical_AI/images/sample.png")

rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

cv2.imshow("Original BGR Image", image)
cv2.imshow("Converted RGB Image", rgb_image)

cv2.waitKey(0)
cv2.destroyAllWindows()