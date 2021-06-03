import cv2
sun_img = cv2.imread("sun.jpg")
sea_img = cv2.imread("sea.jpeg")
sun_img_re = cv2.resize(sun_img,(400,300))
sea_img_re = cv2.resize(sea_img,(400,300))
img = cv2.vconcat([sun_img_re,sea_img_re])
cv2.imshow("Merged Vertically", img)
cv2.waitKey()
cv2.destroyAllWindows()
