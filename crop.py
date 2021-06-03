import cv2
photo = cv2.imread("twomantalking.jpg")
crop_photo=photo[20:200,450:600] 
photo[20:200,650:800] = crop_photo
cv2.imshow("pic swap",photo)
cv2.waitKey()
cv2.destroyAllWindows()
