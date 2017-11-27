import cv2
import numpy as np

img=cv2.imread("Projects/object detector/real.jpg")

temp=cv2.imread("templ.jpg",0)

gry=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

w,h=temp.shape[::-1]

res = cv2.matchTemplate(gry,temp,cv2.TM_CCOEFF_NORMED)

threshold = 0.7

loc = np.where( res >= threshold)

for pt in zip(*loc[::-1]):
    
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (69,69,69), 1)
    #MY FAV RGB CODE







cv2.imshow("Detected",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
