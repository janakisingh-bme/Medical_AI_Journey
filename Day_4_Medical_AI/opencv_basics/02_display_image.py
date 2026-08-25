import cv2

image = cv2.imread("Day_4_Medical_AI/images/sample.png")

cv2.imshow("Medical X-Ray", image)

cv2.waitKey(0)
cv2.destroyAllWindows()