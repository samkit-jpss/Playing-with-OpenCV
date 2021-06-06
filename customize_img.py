import cv2
import numpy as np 
img = np.zeros([512,512,3])
c1_img = cv2.circle(img,(100,100),70,(0,255,255),-1)
c2_img = cv2.circle(c1_img,(400,100),70,(0,255,255),-1)
n_img = cv2.rectangle(c2_img,(0,200),(512,512),(255,8,0),-1)
f_img = cv2.rectangle(n_img,(100,450),(400,350),(0,255,0),-1)

cv2.imshow("Ninja Turtle",f_img)
cv2.waitKey()
cv2.destroyAllWindows()
