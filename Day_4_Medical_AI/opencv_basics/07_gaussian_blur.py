import cv2

image = cv2.imread("Day_4_Medical_AI/images/sample.png")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

cv2.imshow("Original X-Ray", image)
cv2.imshow("Grayscale X-Ray", gray_image)
cv2.imshow("Blurred X-Ray", blurred_image)

cv2.waitKey(0)
cv2.destroyAllWindows()