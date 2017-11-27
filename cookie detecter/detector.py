import cv2
import numpy as np
#importing libs

img=cv2.imread("Projects/object detector/real.jpg")
#reading the orignal image 

temp=cv2.imread("templ.jpg",0)
#importing template image ,already grayscaled

gry=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#converting to gray

w,h=temp.shape[::-1]
#setting w,h to the width and height dimensions of the template image

res = cv2.matchTemplate(gry,temp,cv2.TM_CCOEFF_NORMED)
#our template matching func using CCOEFF_NORMED method

threshold = 0.7
#just to set aukat

loc = np.where( res >= threshold)

#just 'for' detecting multiple occurrences
for pt in zip(*loc[::-1]):
    
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (69,69,69), 1)
    #MY FAV RGB CODE
    
cv2.imshow("Detected",img)

cv2.waitKey(0)

cv2.destroyAllWindows()

